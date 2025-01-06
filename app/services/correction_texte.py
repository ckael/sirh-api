#pip install language-tool-python

import language_tool_python

# Initialiser l'outil de vérification grammaticale pour le français
language_tool = language_tool_python.LanguageTool('fr-FR')

# Texte à corriger
text = "bojour tous le monde"

# Détecter les erreurs
errors = language_tool.check(text)

# Appliquer les corrections
corrected_text = text
for error in errors:
    corrected_text = corrected_text.replace(error.context, error.replacements[0]) if error.replacements else corrected_text

# Afficher les résultats
print("Texte à corriger :", text)
print(f"Erreurs trouvées ({len(errors)}) :")
for error in errors:
    print(f"- {error.message}: '{error.context}' (suggestion : {', '.join(error.replacements)})")
print("Correction :", corrected_text)