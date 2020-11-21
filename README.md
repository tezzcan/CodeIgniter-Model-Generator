# CodeIgniter Model Generator
A very basic and hackable CodeIgniter4 model generator. Feel free to add cool features.

Input file has to be a .txt file exported by phpMyAdmin.

### Usage

```sh
modelMaker.py [-h] -i INPUT -t TABLE_NAME [-p PASS_COUNT]

optional arguments:
  -h, --help            show this help message and exit
  -i INPUT, --input INPUT
                        provide an .txt file
  -t TABLE_NAME, --table-name TABLE_NAME
                        provide a table name
  -p PASS_COUNT, --pass-count PASS_COUNT
                        how many line will be passed? (def=none)
```

### Sample Output
```sh
<?php
namespace App\Models;
use \CodeIgniter\Model;
class UsersModel extends Model {
	protected $table = 'users';
	protected $primaryKey = 'id';
	protected $allowedFields = ['col1','col2'];
}
?>
```
