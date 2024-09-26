
class SimpleReflexAgent:
 def __init__(self,desired_temp):
  self.desired_temp = desired_temp

 def percept(self,current_temp):
  self.current_temp =current_temp

 def act(self):
  if self.current_temp > self.desired_temp:
   return "turn off the Heater"
  else:
   return "turn on the Heater"
  
room = {
 "Living Room":28,
 "Bed Room":18,
 "Kitchen":30,
}
agent=SimpleReflexAgent(22)

for room_name,temp in room.items():
  action=agent.percept(temp)
  print(f"{room_name} (Temp:{temp})==>{agent.act()}")
  

