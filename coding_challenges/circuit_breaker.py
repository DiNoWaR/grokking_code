import time

# Ключевые моменты:
#  3 состояния системы: Открытое, Полуоткрытрое, Закрытое
#  В системе есть поля: время последнего фейла, количество допустимых ошибок, время восстановления
#  Закрытое: система пропускает все запросы
#  Открытое: система блокирует все запросы
#  Полуоткрытрое: система пропускает все запросы, но если ошибка, то снова переходит в Открытое
#  При очередном запросе если состояние open, то проверяем прошел ли recovery timeout, если да то переводим в Полуоткрытрое

class CircuitBreaker:
    def __init__(self, failures_threshold=5, recovery_timeout=10):
        self.failures_threshold = failures_threshold
        self.recovery_timeout = recovery_timeout
        self.failures = 0
        self.last_failure_time = None
        self.state = 'closed'  # 'closed', 'open', 'half_open'

    def call(self, func, *args, **kwargs):
        if self.state == 'open':
            if time.time() > self.last_failure_time + self.recovery_timeout:
                self.state = 'half_open'
            else:
                raise Exception('Circuit breaker has already been opened')
        try:
            result = func(*args, **kwargs)
            self.reset()
            return result
        except Exception as e:
            self.record_failure()
            raise e

    def record_failure(self):
        self.failures += 1
        if self.failures >= self.failures_threshold:
            self.state = 'open'
        self.last_failure_time = time.time()

    def reset(self):
        self.failures = 0
        self.state = 'closed'
