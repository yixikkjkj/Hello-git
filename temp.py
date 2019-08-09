import blinker

signal = blinker.Namespace()

test_signal = signal.signal('test_singal_one')


@test_signal.connect
def once_signal_sent(param_one, param_two, *args, **kwargs):
    print(param_one)
    print(param_two)
    print(args)
    print(kwargs)


if __name__ == "__main__":
    test_signal.send({
        'param_one': 1,
        'param_two': 'two',
        'other': 'nonononono',
    })


{
    bAlert ? (
    <Button>
        查看任务列表
    </Button>
    ) : ''
}

{
    '_id': ObjectId('5ceb967f4f9fc9321a88ab59'),
    'created_t': datetime.datetime(2019, 5, 27, 15, 49, 19, 646000),
    'balance': 97550,
    'frozen': 1295,
    'used': 1155,
    'user_name': 'taovip',
    'password_hash':
    'pbkdf2:sha256:150000$Ziw7ZC8L$e2fda666129c5abd8e512eea8136ef407beb0699df92ab640bfbae1de78eebbe',
    'last_login': datetime.datetime(2019, 5, 27, 15, 49, 19, 646000)
}
{
    'name': '活动 910035',
    'text': '【Hand Of God】test for回T退订',
    'schedule_t': datetime.datetime(2019, 8, 6, 15, 15),
    'plan_type': 2,
    'cache_key': 'mobile_upload_5ceb967f4f9fc9321a88ab59_1565075436649_226',
    'user_id': ObjectId('5ceb967f4f9fc9321a88ab59')
}
