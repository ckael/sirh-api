from transformers import pipeline


def resume(texte):

    # Initialiser le pipeline pour la summarization
    summarizer = pipeline("summarization")

    # Générer le résumé
    resume = summarizer(
        texte,
        max_length=100,
        min_length=50,
        do_sample=False
    )

    resume_text = resume[0]['summary_text']

    # Afficher le résultat
    return resume_text
