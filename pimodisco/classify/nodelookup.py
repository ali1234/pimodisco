import re
import tensorflow as tf
import operator

class NodeLookup(object):
    """Converts integer node ID's to human readable labels."""

    def __init__(self, imagenet):

        label_lookup_path = str(imagenet / 'imagenet_2012_challenge_label_map_proto.pbtxt')
        uid_lookup_path = str(imagenet / 'imagenet_synset_to_human_label_map.txt')

        self.is_a = dict()
        with open(str(imagenet / 'wordnet.is_a.txt')) as is_a:
            for line in is_a:
                a,b = line.split()
                self.is_a[b] = a

        if not tf.gfile.Exists(uid_lookup_path):
            tf.logging.fatal('File does not exist %s', uid_lookup_path)
        if not tf.gfile.Exists(label_lookup_path):
            tf.logging.fatal('File does not exist %s', label_lookup_path)

        # Loads mapping from string UID to human-readable string
        proto_as_ascii_lines = tf.gfile.GFile(uid_lookup_path).readlines()
        self.uid_to_human = {}
        p = re.compile(r'[n\d]*[ \S,]*')
        for line in proto_as_ascii_lines:
            parsed_items = p.findall(line)
            uid = parsed_items[0]
            human_string = parsed_items[2]
            self.uid_to_human[uid] = human_string

        # Loads mapping from string UID to integer node ID.
        self.node_id_to_uid = {}
        proto_as_ascii = tf.gfile.GFile(label_lookup_path).readlines()
        for line in proto_as_ascii:
            if line.startswith('  target_class:'):
                target_class = int(line.split(': ')[1])
            if line.startswith('  target_class_string:'):
                target_class_string = line.split(': ')[1]
                self.node_id_to_uid[target_class] = target_class_string[1:-2]


    def id_to_string(self, node_id):
        if node_id not in self.node_id_to_uid:
            return 'Unknown'
        result = []
        node_uid = self.node_id_to_uid[node_id]
        while node_uid in self.uid_to_human and node_uid in self.is_a:
            result.append(self.uid_to_human[node_uid])
            node_uid = self.is_a[node_uid]
        return ' / '.join(reversed(result))

