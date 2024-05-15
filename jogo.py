while len(word_letters) > 0 and lives > 0:
    word_letters = set(word)

    # Mostrando as letras já utilizadas
    print("Letras já usadas: ", " ".join(used_letters))

    # Mostrando a palavra com as letras reveladas e espaços para as letras desconhecidas
    word_list = [letter if letter in used_letters else "_" for letter in word]
    print(" ".join(word_list))

    # Perguntando ao jogador pela próxima letra
    user_letter = input("Digite uma letra: ").lower()

    if user_letter in alphabet - used_letters:
        used_letters.add(user_letter)

        if user_letter in word_letters:
            word_letters.remove(user_letter)
            print("Letra correta!")
        else:
            lives -= 1
            print(f"Letra errada. Você ainda tem {lives} vidas restantes.")
            print(stages[lives])  # Exibindo a imagem da forca atualizada

    elif user_letter in used_letters:
        print("Você já digitou essa letra. Tente novamente!")

    else:
        print("Letra inválida. Digite apenas letras entre 'a' e 'z'.")

if lives == 0:
    print(f"Você perdeu! A palavra era {word}.")
    print(stages[0])  # Exibindo a imagem final da forca
elif len(word_letters) == 0:
    print(f"Parabéns! Você acertou a palavra {word}.")
