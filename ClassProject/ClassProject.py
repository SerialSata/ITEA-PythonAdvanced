import fcntl


def write_base(name, phone_num):
    with open('PhoneBook.txt', 'at') as base:
        fcntl.lockf(base, fcntl.LOCK_EX)
        base.write('{name:phone_num}')
        fcntl.lockf(base, fcntl.LOCK_UN)


################################################################

class CSV:
    def load(self):
        print('CSV load')
        return {'Bill': '911'}

    def save(self, d):
        print('CSV save')


class JSON:
    def load(self):
        print('Json load')
        return {'Bill': '911'}

    def save(self, d):
        print('JSON save')


CONFIG = {
    'dumper': 'CSV'
}

if CONFIG['dumper'] == 'CSV':
    dumper = CSV()
elif CONFIG['dumper'] == 'JSON':
    dumper = JSON()

phonebook = dumper.load()

# MODEL CODE

dumper.save(phonebook)
