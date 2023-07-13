class SentimentAnalysisEntity:
    def __init__(self, text):
        self.text = text


class TopicModellingEntity:
    def __init__(self, topics, text):
        self.topics = topics
        self.text = text


class EmailClassificationEntity:
    def __init__(self, sent_from, subject, body):
        self.sent_from = sent_from
        self.subject = subject
        self.body = body
