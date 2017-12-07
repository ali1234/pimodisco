from pimodisco.classify.classify import *

def main(*args):
    print(args)
    run_inference_on_file(args[0][1])

if __name__ == '__main__':
    import sys
    tf.app.run(main=main, argv=sys.argv)
