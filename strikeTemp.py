
grain = 5.5
gallons = 3
quarts = gallons * 4.0
ratio = quarts / grain 
initTemp = 69.0 # grain temp
targetTemp = 155.0 


def computeStrikeTemp():
  strikeTemp = (0.2 / ratio) * (targetTemp - initTemp) + targetTemp
  print "(0.2 / %.1f) * (%.1f - %.1f) + %.1f" % (ratio, targetTemp, initTemp, targetTemp)
  print "strikeTemp = %.1f" % strikeTemp

# Note if using a mash tun overheat by 5-7 degrees
# or pre-heat with a gallon of near boiling water

def main():
  global grain, initTemp, targetTemp
  grain = float(raw_input("Amount of grains (lbs):"))
  initTemp = float(raw_input("Current grain temp: "))
  targetTemp = float(raw_input("Target mash temperature (155 F Default):"))
  computeStrikeTemp()

if __name__ == '__main__':
  main()

