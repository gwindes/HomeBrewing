# import sys

def convertLME(lme):
  lme = float(lme)
  dme = lme * 0.8
  grains = lme / 0.75
  printData(lme, dme, grains)
  # print "LME: %0.2f lbs" % lme
  # print "DME: %0.2f lbs" % dme
  # print "Grains: %0.2f lbs" % grains

def convertDME(dme):
  dme = float(dme)
  lme = dme / 0.8
  grains = dme / 0.6
  printData(lme, dme, grains)
  # print "DME: %0.2f lbs" % dme
  # print "LME: %0.2f lbs" % lme
  # print "Grains: %0.2f lbs" % grains

def convertGrain(grains):
  grains = float(grains)
  points =  (grains * 36) * 0.7
  lme = grains * 0.75
  dme = grains * 0.6
  dmePoints = points / 44
  lmePoints = points / 36
  printData(lme, dme, grains)
  # print "Grains: %s lbs" % grains
  # print "points = %0.2f" % points
  # print "LME: %s lbs" % lme
  # print "DME: %s lbs" % dme
  # print "LME Points: %0.2f lbs" % lmePoints
  # print "DME Points: %0.2f lbs" % dmePoints

def printData(lme, dme, grains):
  print "LME: %0.2f lbs" % lme
  print "DME: %0.2f lbs" % dme
  print "Grains: %0.2f lbs" % grains

def errhandler():
  print "Your input has not been recognized"
  
if __name__ == '__main__':
  print "Select which item to convert from:"
  selectedType = raw_input("1. Grains \n2. DME \n3. LME \nType = ")
  amount = raw_input("\nInput amount in lbs: ")

  if selectedType is 1:
    pass

  convertType = {
    1: convertGrain,
    2: convertDME,
    3: convertLME
  }

  convertType.get(int(selectedType))(amount)