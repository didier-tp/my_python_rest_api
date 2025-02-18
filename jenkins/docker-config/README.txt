[sudo] docker compose --profile python up -d
NB: avec le profil "python" , un seul agent est créé (en version python) et donc agent any est ok .

[sudo] docker compose --profile python down -v --remove-orphans