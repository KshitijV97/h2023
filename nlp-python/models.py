class SentimentAnalysisEntity:
    def __init__(self, text):
        self.text = text


class TopicModellingEntity:
    def __init__(self, topics, text):
        self.topics = topics
        self.text = text


class EmailClassificationEntity:
    def __init__(self, subject, body):
        self.subject = subject
        self.body = body
