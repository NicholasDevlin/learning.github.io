def announce(f):
  def wrapper():
    print("wait..")
    f()
    print("done")
  return wrapper

@announce
def hello():
  print("hello world")

hello()