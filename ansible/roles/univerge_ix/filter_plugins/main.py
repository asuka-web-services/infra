from typing import Any, Callable

Path = tuple[str, ...]
Mode = Path

class Command:
  def __init__(self, mode: Mode, command: str) -> None:
    self.__mode = mode
    self.__command = command
    self.__path = mode + (command,)

  def get_mode(self) -> Mode:
    return self.__mode

  def get_command(self) -> str:
    return self.__command

  def get_path(self) -> Path:
    return self.__mode + (self.__command,)

  def __eq__(self, other: object) -> bool:
    if not isinstance(other, Command):
      return NotImplemented
    return self.get_path() == other.get_path()

  def __hash__(self) -> int:
    return hash(self.get_path())

class Config:
  def __init__(self, config_text: str) -> None:
    self.__config_text = config_text

  def to_be(self, desired_config: 'Config') -> list[str]:
    self_commands = self._to_commands()
    desired_commands = desired_config._to_commands()
    added_commands = desired_commands - self_commands
    deleted_commands = self_commands - desired_commands
    optimized_deleted_commands = self._remove_redundant_child_paths(deleted_commands)

    mode_order: list[Mode] = sorted(
      {cmd.get_mode() for cmd in added_commands | optimized_deleted_commands},
      key=lambda mode: (len(mode), mode)
    )
    apply_commands: list[str] = []

    for current_mode in mode_order:
      apply_commands.append('configure')
      for parent in current_mode:
        apply_commands.append(parent)

      deleted_commands_on_current_mode = sorted(
        (cmd for cmd in optimized_deleted_commands if cmd.get_mode() == current_mode),
        key=lambda cmd: cmd.get_command()
      )
      for command in deleted_commands_on_current_mode:
        apply_commands.append('no ' + command.get_command())

      added_commands_on_current_mode = sorted(
        (cmd for cmd in added_commands if cmd.get_mode() == current_mode),
        key=lambda cmd: cmd.get_command()
      )
      for command in added_commands_on_current_mode:
        apply_commands.append(command.get_command())

    return apply_commands

  def _to_commands(self) -> set[Command]:
    commands: set[Command] = set()
    current_path: Path = ()

    for line in self.__config_text.splitlines():
      stripped_line = line.replace('\r', '').strip()
      if not stripped_line or stripped_line.startswith('!'):
        continue

      indent = (len(line) - len(line.lstrip())) // 2
      current_path = current_path[:indent] + (stripped_line,)
      commands.add(Command(
        mode=current_path[:-1],
        command=current_path[-1]
      ))
      
    return commands

  def _remove_redundant_child_paths(self, commands: set[Command]) -> set[Command]:
    path_set = {command.get_path() for command in commands}
    optimized_commands: set[Command] = set()
    for command in commands:
      path = command.get_path()
      ancestor_exists = any(path[:i] in path_set for i in range(1, len(path)))
      if not ancestor_exists:
        optimized_commands.add(command)
    return optimized_commands

class FilterModule:
  def filters(self) -> dict[str, Callable[..., Any]]:
    return {
      'to_be': self.to_be
    }

  def to_be(self, running_config_text: str, desired_config_text: str) -> list[str]:
    running_config = Config(running_config_text)
    desired_config = Config(desired_config_text)
    return running_config.to_be(desired_config)
