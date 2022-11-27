from abc import ABC, abstractmethod

class Parser(ABC):
    def parse(self):
        self._parse()
    @abstractmethod
    def _parse(self):
        pass

class WanteedParser(Parser):
    url = 'https://www.wanted.co.kr/'
    def _parse(self):
        print(self.url)

class CatchParser(Parser):
    url = 'https://www.catch.co.kr/'
    def _parse(self):
        print(self.url)


a = WanteedParser()
a.parse()

b = CatchParser()
b.parse()
# 템플릿 메서드 패턴
# 의존성 폭발 -> Parser에서 하나의 메서드가 추가될 경우 모든 경우의 자식 클래스를 변경해야됌



class Strategy(ABC):
    @abstractmethod
    def parse(self):
        pass

class Content():
    def __init__(self, strategy: Strategy) -> None:
        self._strategy = strategy

    def parse(self):
        self._strategy.parse(self._strategy)
`
class WanteedContent(Strategy):
    url = 'https://www.wanted.co.kr/'
    def parse(self):
        print(self.url)

class CatchContent(Strategy):
    url = 'https://www.catch.co.kr/'
    def parse(self):
        print(self.url)

a = Content(WanteedContent)
a.parse()
b = Content(CatchContent)
b.parse()

# 소유격인 전략패턴.
# 자유롭게 Strategy를 변경하면서 구현할 수 있고, 조합성이 폭발하지만 cut-off 로 관리할 수 있음.

