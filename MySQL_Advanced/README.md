# MySQL Advanced

Ce référentiel contient des scripts SQL qui illustrent diverses tâches avancées en utilisant MySQL. Chaque tâche est accompagnée de son propre script SQL et d'un exemple de son exécution.

## Task

### 0. We are all unique!

Ce script SQL crée une table `users` avec des attributs spécifiés et garantit que l'attribut `email` est unique.

### 1. In and not out

Ce script SQL crée une table `users` avec des attributs spécifiés, y compris un attribut `country` qui est une énumération de certains pays. Il assure également que l'attribut `email` est unique.

### 2. Best band ever!

Ce script SQL crée une table `users` suivant certaines exigences. Il importe également un fichier de données et classe les origines des groupes de musique en fonction du nombre de fans.

### 3. Old school band

Ce script SQL liste tous les groupes de musique avec le style "Glam rock" comme leur style principal, classés par leur longévité.

### 4. Buy buy buy

Ce script SQL crée un déclencheur qui diminue la quantité d'un article après avoir ajouté une nouvelle commande.

### 5. Email validation to sent

Ce script SQL crée un déclencheur qui réinitialise l'attribut `valid_email` uniquement lorsque l'e-mail a été modifié.

### 6. Add bonus

Ce script SQL crée une procédure stockée `AddBonus` qui ajoute une nouvelle correction pour un étudiant donné.

### 7. Average score

Ce script SQL crée une procédure stockée `ComputeAverageScoreForUser` qui calcule et stocke la moyenne des notes pour un étudiant donné.

### 9. Optimize search and score

Ce script SQL crée un index `idx_name_first_score` sur la table `names` pour indexer uniquement la première lettre du nom et la note.

### 10. Safe divide

Ce script SQL crée une fonction `SafeDiv` qui divise deux nombres et retourne 0 si le deuxième nombre est égal à 0.

### 11. No table for a meeting

Ce script SQL crée une vue `need_meeting` qui liste tous les étudiants ayant une note inférieure à 80 et aucun `last_meeting` ou plus d'un mois.

---