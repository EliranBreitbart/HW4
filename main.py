# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import DAOs_DTOs
from repository import repo
import sys


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def load_config(f):
    with open(f) as _f:
        line = _f.readline()
        x = line.split(',')
        for _ in range(int(x[0])):
            hat = _f.readline().replace('\n', '')
            repo.hats.insert(DAOs_DTOs.HatDTO(*hat.split(",")))
        for _ in range(int(x[1])):
            supplier = _f.readline().replace('\n', '')
            repo.suppliers.insert(DAOs_DTOs.SupplierDTO(*supplier.split(",")))


def execute_orders(f):
    summary = open(sys.argv[3], 'r+')
    summary.truncate(0)
    counter = 1
    with open(f) as _f:
        line = _f.readline()
        all_hats = repo.hats.query_all()
        suppliers = repo.suppliers.query_all()
        while line:
            topping = line.split(',')[1].replace('\n', '')
            hat = filter(lambda x: x.topping == topping, all_hats).__next__()
            if hat.quantity > 0:
                hat.quantity -= 1
                repo.hats.update(hat)
                supplier = filter(lambda x: x.id == hat.supplier, suppliers).__next__()
                summary.write(topping + "," + supplier.name + "," + line.split(',')[0] + "\n")
                repo.orders.insert(DAOs_DTOs.OrderDTO(counter, line.split(',')[0], hat.id))
                counter += 1
                line = _f.readline()
                if hat.quantity == 0:
                    repo.hats.delete(hat)
                    all_hats.remove(hat)

    summary.close()


if __name__ == '__main__':
    repo.create_tables()
    load_config(sys.argv[1])
    execute_orders(sys.argv[2])
    print('finished')

