from motor_inferencia import inferir


def iniciar_chatbot():

    print("=" * 50)
    print("CHATBOT - DÍA DE MUERTOS")
    print("=" * 50)

    print(
        "\nHola, soy un sistema experto sobre el Día de Muertos."
    )

    print(
        "Puedes preguntarme sobre altares, flores, velas, "
        "pan de muerto, calaveritas y fechas."
    )

    print("\nEscribe 'salir' para terminar.\n")

    while True:

        mensaje = input("Tú: ")

        if mensaje.lower().strip() == "salir":
            print("\nChatbot: Hasta luego.")
            break

        respuesta = inferir(mensaje)

        print(f"\nChatbot: {respuesta}\n")


if __name__ == "__main__":
    iniciar_chatbot()