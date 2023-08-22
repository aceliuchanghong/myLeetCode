from fromBook.util.ChangeTwo import exchange
from fromBook.util.generateArray import newArray

data = newArray.generateit(10)
print(data)
data[0], data[9] = exchange(data[0], data[9])
print(data)
