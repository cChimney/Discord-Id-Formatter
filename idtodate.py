from py_mini_racer import py_mini_racer
import time, datetime

start_time = time.time()

ctx = py_mini_racer.MiniRacer()

def checkDate(id):
    script = """
    function convert(id=%s) {
        var bin = (+id.toString()).toString(2);
        var unixbin = '';
        var unix = '';
        var m = 64 - bin.length;
        unixbin = bin.substring(0, 42-m);
        unix = parseInt(unixbin, 2) + 1420070400000;
        return unix;
    }
    """ % (id)
    ctx.eval(script)
    val = ctx.call("convert")
    return val

def worker(age):
    Older = []
    ids = open('ids.txt').read().splitlines()
    unixAge = int(time.mktime(datetime.datetime.strptime(age, "%d/%m/%Y").timetuple()))*1000
    for id in ids:
        idAge = checkDate(id)
        if int(unixAge) > int(idAge):
            Older.append(id)
    with open('olderIds.txt', 'a+') as f:
        for id in Older:
            f.write(f"{id}\n")
    print(f'Took {time.time() - start_time}s to sort {len(ids)} ids\nTool made by https://github.com/cChimney')

try:
    print("ID Sorter, made by cChimney. https://github.com/cChimney")
    age = input("Save ids that are older than what date? Example 15/12/2015 (european dates)\n> ")
    worker(age)
except Exception as err:
    print(err)
