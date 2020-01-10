import Machine
import Configure
import FeaturesSelection

def usage():
    pass


def main():
  predictor = Machine(MAX_WORD_LENGTH, "../data/", Configure.PREDICT)
  predictor.load('dongdu.model', 'dongdu.map')
  print('Load successful.')

main()
