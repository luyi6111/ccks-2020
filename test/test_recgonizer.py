def add_root_path():
    import sys
    from pathlib import Path
    cur_dir = Path(__file__).absolute().parent
    times = 10
    while not str(cur_dir).endswith('ccks-2020') and times:
        cur_dir = cur_dir.parent
        times -= 1
    print(cur_dir)
    sys.path.append(str(cur_dir))


add_root_path()
from ckbqa.dataset.data_prepare import load_data
from ckbqa.models.recognizer import Recognizer
from ckbqa.utils.logger import logging_config
import logging

logging_config('test.log', stream_log=True)


def test_recgnizer():
    print('start')
    logging.info('test start ...')
    recognizer = Recognizer()
    for q, sparql, a in load_data():
        q_text = q.split(':')[1]
        rec_entities = recognizer.find_entities(q_text)
        print(rec_entities)
        print(q)
        print(sparql)
        print(a)
        import ipdb
        ipdb.set_trace()


if __name__ == '__main__':
    test_recgnizer()
