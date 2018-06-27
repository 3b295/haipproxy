"""
We use this validator to filter ip that can access mobile zhihu website.
"""
from haipproxy.config.settings import (
    TEMP_AMAZON_QUEUE, VALIDATED_AMAZON_QUEUE,
    TTL_AMAZON_QUEUE, SPEED_AMAZON_QUEUE)
from ..redis_spiders import ValidatorRedisSpider
from .base import BaseValidator


class AmazonValidator(BaseValidator, ValidatorRedisSpider):
    """This validator checks the liveness of amazon proxy resources"""
    name = 'amazon'
    urls = [
        'https://www.amazon.com/',
    ]
    task_queue = TEMP_AMAZON_QUEUE
    score_queue = VALIDATED_AMAZON_QUEUE
    ttl_queue = TTL_AMAZON_QUEUE
    speed_queue = SPEED_AMAZON_QUEUE
    # 判断success_key是否在响应内容中，从而判断IP是否正常，默认为''，表示正常
    success_key = ''

    # 父类校验方法
    # def is_ok(self, response):
    #     return True if self.success_key in response.text and 'python' in response.text else False