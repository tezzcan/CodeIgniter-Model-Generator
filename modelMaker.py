import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--input", required=True,help="provide an .txt file")
ap.add_argument("-t", "--table-name", required=True,help="provide a table name")
ap.add_argument("-p", "--pass-count", required=False,help="how many line will be passed? (def=none)")
args = vars(ap.parse_args())

TABLENAME = args['table_name']
PASSCOUNT = args['pass_count']


with open(f'{args["input"]}', 'r') as f:
    dummy = f.readlines()


dummyArr = []
def beatufiy(x = 0):
    counter = 0
    for item in dummy:
        try:
            if counter <= x:
                counter += 1
                continue
            dummyArr.append(item.split('|')[1])
        except:
            pass

beatufiy(int(PASSCOUNT)) if PASSCOUNT else beatufiy()

with open(f'{args["table_name"]}.php', 'w') as f:
    f.write('<?php\n')
    f.write('namespace App\Models;\n')
    f.write('use \CodeIgniter\Model;\n')
    f.write('class {}'.format(TABLENAME) + 'Model extends Model {\n')
    f.write("\tprotected $table = '{}';\n".format(TABLENAME))
    f.write("\tprotected $primaryKey = 'id';\n")
    f.write("\tprotected $allowedFields = ")
    f.write('[')
    for item in dummyArr:
        if dummyArr.index(item) == len(dummyArr) - 1:
            f.write("'" + item + "'")    
        else:
            f.write("'" + item + "',")
    f.write('];\n}\n?>')

print('\n--DONE--')