class Flight():
  def __init__(self, capacity):
    self.capacity = capacity
    self.passangers = []

  def add_passenger(self, name):
    if not self.open_seats():
      return False
    self.passangers.append(name)
    return True

  def open_seats(self):
    return self.capacity - len(self.passangers)

flight = Flight(3)

people = ["me", "lia", "ndc", "lily"]

for person in people:
  if flight.add_passenger(person):
    print(f"{person} is added to this flight successfully.")
  else:
    print(f"no available seats for {person}.")