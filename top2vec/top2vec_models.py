from top2vec import Top2Vec

def reduce_model(t2v_model, num_topics_reduce):

    topic_nums = t2v_model.get_num_topics()

    if topic_nums < num_topics_reduce:
        print(f"No reduction possible as the current number of topics is smaller than the requested reduced number of topics.")
    else:
        t2v_model.hierarchical_topic_reduction(num_topics=num_topics_reduce)

    return t2v_model

def top_k_topics_word_clouds(t2v_model, num_topics=5, reduced=False):
    for topic in range(num_topics):
        t2v_model.generate_topic_wordcloud(topic,reduced=reduced)
    return 

def find_closest_topics_keyword(t2v_model, keyword, num_closest_topics=5, gen_word_clouds=False, reduced=False):

    topic_words, word_scores, topic_scores, topic_nums = t2v_model.search_topics(keywords=[keyword], num_topics=num_closest_topics, reduced=reduced)

    if gen_word_clouds==True:
        for topic in topic_nums:
            t2v_model.generate_topic_wordcloud(topic, reduced=reduced)

    return topic_words, word_scores, topic_scores, topic_nums

def find_representative_docs(t2v_model, topic_num, num_docs=5, reduced=False, print_docs=False):

    documents, document_scores, document_ids = t2v_model.search_documents_by_topic(topic_num=topic_num, num_docs=num_docs, reduced=reduced)

    if print_docs==True:
        for doc, score, doc_id in zip(documents, document_scores, document_ids):
            print(f"Document: {doc_id}, Score: {score}")
            print("-----------")
            print(doc)
            print("-----------")
            print()
        
    return documents, document_scores, document_ids

def find_closest_semantic_doc_keywords(t2v_model, keyword, num_docs=5, print_docs=False):

    documents, document_scores, document_ids = t2v_model.search_documents_by_keywords(keywords=[keyword], num_docs=num_docs)

    if print_docs==True:
        for doc, score, doc_id in zip(documents, document_scores, document_ids):
            print(f"Document: {doc_id}, Score: {score}")
            print("-----------")
            print(doc)
            print("-----------")
            print()

    return documents, document_scores, document_ids

def find_similar_keywords(t2v_model, keyword, num_words=20, print_words=False):

    words, word_scores = t2v_model.similar_words(keywords=[keyword], keywords_neg=[], num_words=num_words)

    if print_words==True:
        for word, score in zip(words, word_scores):
            print(f"Word: {word}, Score: {score}")

    return words, word_scores

def get_most_representative_topics(t2v_model, doc_id, num_topics=5, reduced=False, gen_word_clouds=False):

    topics , topic_scores , topics_words, word_scores   = t2v_model.get_documents_topics([doc_id], num_topics=num_topics, reduced=reduced)

    if gen_word_clouds==True:
        for topic in topics[0]:
            t2v_model.generate_topic_wordcloud(topic, reduced=reduced)

    return topics , topic_scores , topics_words, word_scores



    