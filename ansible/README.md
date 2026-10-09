# ansible

## 実行

```
ansible-playbook --ask-vault-pass -i production/hosts.yml -CD site.yml --limit {limitfilter}
ansible-playbook --ask-vault-pass -i production/hosts.yml -D site.yml --limit {limitfilter}
```

## シークレットの作り方

```
ansible-vault encrypt_string '{plaintext}'
```
