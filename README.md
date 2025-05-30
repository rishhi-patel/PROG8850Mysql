# PROG8850Week1Installation
install mysql, python

```bash
ansible-playbook up.yml
```

To use mysql:

```bash
mysql -u root -h 127.0.0.1 -p
```

To run github actions like (notice that the environment variables default for the local case):

```yaml
      - name: Deploy to Database
        env:
          DB_HOST: ${{ secrets.DB_HOST || '127.0.0.1' }} 
          DB_USER: ${{ secrets.DB_ADMIN_USER || 'root' }}
          DB_PASSWORD: ${{ secrets.DB_PASSWORD  || 'Secret5555'}}
          DB_NAME: ${{ secrets.DB_NAME || 'mysql' }}
        run: mysql -h $DB_HOST -u $DB_USER -p$DB_PASSWORD $DB_NAME < schema_changes.sql
```        

locally:

```bash
bin/act -P ubuntu-latest=-self-hosted
```

To shut down:

```bash
ansible-playbook down.yml
```

This is a reproducible mysql setup
