import spacy

def summarize_text(text, nlp, num_sentences=3):
    doc = nlp(text)
    sentences = [sent for sent in doc.sents]
    sentence_scores = {}

    for sent in sentences:
        for word in sent:
            if word.text.lower() not in nlp.Defaults.stop_words and word.is_alpha:
                if sent in sentence_scores:
                    sentence_scores[sent] += 1
                else:
                    sentence_scores[sent] = 1

    # Get the highest scored sentences
    summarized_sentences = sorted(sentence_scores, key=sentence_scores.get, reverse=True)[:num_sentences]
    summary = ' '.join([str(sent) for sent in summarized_sentences])
    return summary
