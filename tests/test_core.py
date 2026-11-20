from app.core import milestone_1, milestone_2, milestone_3


def test_milestone_1():
    sequences = milestone_1()

    assert len(sequences) == 5
    assert "E001" in sequences
    assert sequences["E001"][0] == "Python"
    assert "Machine Learning" in sequences["E001"]


def test_milestone_2():
    result = milestone_2()

    assert "itemsets" in result
    assert "rules" in result
    assert len(result["itemsets"]) > 0

    frequent_transitions = [
        next(iter(itemset))
        for itemset in result["itemsets"]
        if len(itemset) == 1
    ]

    assert "Python -> SQL" in frequent_transitions


def test_milestone_3(monkeypatch):
    def fake_chat(messages, **options):
        assert "Python" in messages[1]["content"]
        return "Recommended skill: Machine Learning. It builds on Python."

    monkeypatch.setattr("app.core.chat", fake_chat)

    result = milestone_3(["Python", "SQL"])

    assert "Machine Learning" in result


def test_milestone_3_requires_skills():
    try:
        milestone_3([])
        assert False, "Expected ValueError"
    except ValueError:
        pass