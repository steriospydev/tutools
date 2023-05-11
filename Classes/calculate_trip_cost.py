import math

class TripInfo:

  def __init__(self, city, flight_cost, hotel_per_day, car_rental):
      self.city = city
      self.flight_cost = flight_cost
      self.hotel_per_day = hotel_per_day
      self.car_rental = car_rental

  def cost(self, days):
      week = math.ceil(days / 7)
      cost = self.flight_cost + (days * self.hotel_per_day) + (week * self.car_rental)
      return cost



