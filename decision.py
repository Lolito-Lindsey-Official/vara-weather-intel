# decision pipeline of the vara app

def decision_engine(description, temp, wind, humidity, visibility):
  if wind > 5:
    return "Windy conditions"
  elif "rain" in description:
    return "Bring rain gear"
  elif "snow" in description:
    return "Bring snow gear"
  elif temp < 0:
    return "Freezing conditions"
  elif temp > 37: 
    return "Scorching conditions"
  elif humidity > 60:
    return "Humid conditions"
  elif visibility < 2000:
    return "Poor visibility"
  else: 
    return "Conditions look fine"