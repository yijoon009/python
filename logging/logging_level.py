import logging


if __name__ == '__main__':
    logger = logging.getLogger('main')
    # python 3.7 이전
    # logging.setLevel(logging.INFO)
    # python 3.7 이후
    logging.basicConfig(level=logging.DEBUG)

    # stream handler는 my.log에 파일로 출력하겠다라는 내용
    stream_handler = logging.FileHandler(
        'my.log', mode='a', encoding='utf8')
    logger.addHandler(stream_handler)

        
    logging.debug('틀렸어')
    logging.info('확인해')
    logging.warning('조심해')
    logging.error('에러났어')
    logging.critical('망했다')



    