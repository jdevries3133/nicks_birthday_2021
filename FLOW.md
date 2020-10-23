# Brainstorm

## PNG File / Images

- Hide chunk of data in .png file, by creating an arbitrary unnecessary chunk
    according to the png file format specification.

        - Have a picture from a certain date and time

            - represent the image as a 2D array

            - start the hidden message at the date in the array

- Hiding messages in lowest order bytes

    - rgb(255, 255, 255) => can't change any given value

        - worst case, you change black to yellow

    - rgb(255, 255,  0) => ascii range 60-90

        - worse case, change to rgb(255, 255, 90) => haven't changed the color
            too much

- Simple visual puzzle: you need to separate the rgb channels to see the message
    in the image; [for example](https://en.wikipedia.org/wiki/File:Steganography.png)

## WAV / Audio

- [Hide written message in spectrogram](https://upload.wikimedia.org/wikipedia/commons/5/57/Wikipedia_wavefile_by_Coagula_-_logarihtmic_spectrogram.svg)


# Flow

## Act 1

### Atmosphere / Vibe

"A fake out." Start with a ceaser cypher like a weak ass bitch.


### Flow

1. Start with a clue that references Ceaser himself. Then, show jumbled text:
    instructions to the next step which have been put through a ceaser cypher.


2. Simple web challenge.

    - must load site in the following minutes of the hour: 11, 26, 41, 56

    - ReactJS time troller

        - A web page

        - Will show different messages as the time approaches

        - Silly things like, "you're getting warmer" and "get ready to refresh"

        - Actual clue will be held in a backend API for MAX security. API will
            not even divulge clue in case nick decides to get tricky with us.
            Since Nick will probably get tricky, the api will provide verbose
            messages at the incorrect time which will thoroughly troll Nick
            for all his hard work.

            - Rick roll???

3. "Hope this one doesn't stump you, it's a real enigma!"

    - Enigma code key will be hidden in CSS as an invalid property

>.solution {
>    enigma-code-key: "blah";
>}


## Act 2


### Atmosphere / Vibe

## Act 3




### Atmosphere / Vibe

