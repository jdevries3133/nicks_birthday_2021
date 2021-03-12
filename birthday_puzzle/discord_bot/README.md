# Discord Bot Puzzles

Using python's discord.py

### Bad Math

- Base3 addition using special symbols
- **Prompt:** Why hello there, I have come up with a brand new system of
  mathematics! It features everything you love about old math, addition,
  subtraction, multiplication, and division but with a fun twist. Why don\'t you
  give it a try? Write something that gives you 100 in this NEW MATH and, I\'ll
  give you the key to the next step of this challenge. Fair warning, my numbers
  are dogshit, but you should be able to figure it out.
- **Answer** 100 in the encoded format

### Cyphers

- This section features a set of puzzles using various methods of obsuring
  data Eventually get the key for an encripted message provided for sovling the
  last puzzle. Each step of this puzzle is refered to by the prompts as a "mode"
  each answer should end with `x mode` to indicate the solotion to the puzzle.
  **This will be the only information given to solve these puzzles.**

- [x] Base Mode

- Puzzle created to transition into the cyphers.
- **Prompt:** WOW! nice job with that last one, hope it wasn't too easy. This
  should help you get to the next step
  ["AES encrypted email address"](https://www.devglan.com/online-tools/aes-encryption-decryption)
  Ah shit I don't think that text will proccess properly in my current form. I
  think I have an `austrailian mode`, let's see if that works.
- **Answer** australian mode

- [x] austrailian mode

- **Prompt:** shit I dont thing that worked, It has to be in my dark mode.
  Please be in my dark mode
- Prompt is encoded in [upside down](https://www.upsidedowntext.com/)
- **Answer** dark mode

- [x] Dark mode -**Prompt** Oh fuck I lost it Ok it's Ok lets just try...

- Prompt is encoded in [brail 1](https://www.branah.com/braille-translator)
- **Answer** you decide

The final one should enter AES key mode

- [ ] ESA key mode

**Sub-Steps**

A pass phrase will need to be hashed with SHA256. This digest will be the
256 bit AES key which decrypts the original message. The pass phrase
will be provided by Nick's mom. As an additional twist, the passphrase
will be presented as follows:

> Nice job there Nick! You have almost defeated me, but before you go, I
> wanted to share a message from your mother. She says you smell. Besides that,
> though, I wanted to make sure her message was safe in transit, so I went
> ahead and ran each word through SHA256. Enjoy!
>
> - d0e3df16a7ae644e021b8afe9e56bf1f6d78e4065d786c919a258a61e4b2bd84 (wishing)
> - bb0347a468d97e98a9c00e37cebec1ab930f6f1221cae0f1fbb92b07e1900ba2 (you)
> - ca978112ca1bbdcafac231b39a23dc4da786eff8147c4e72b9807785afee48bb (a)
> - 489f719cadf919094ddb38e7654de153ac33c02febb5de91e5345cbe372cf4a0 (happy)
> - 0422d42c689b7e8046dba2d7042e855f6d21e04464bab168fd263f5b10f893ed (birthday)
> - d7439c4d3981a069260a1b2989d90e549c4c8d7bc62c4f27bc51a7d7a73d90bf (Nick)
> - bb7208bc9b5d7c04f1236a82a0093a5e33f40423d5ba8d4266f7092c3ba43b62 (!)
> - 9f4024faec10ef6d29aa32d7935d94b1a816fd4fe0359fbf12d49d44b5ff33b8 (Love)
> - bcb9dae6ea88dbf28c262998e6661ec60f32a760faa5aef96745b39c38dbf235 (mom)
> - 6fe8ecbc1deafa51c2ecf088cf364eba1ceba9032ffbe2621e771b90ea93153d (dad)
> - 6201111b83a0cb5b0922cb37cc442b9a40e24e3b1ce100a4bb204f4c63fd2ac0 (and)
> - 0ffb02665035bfe509b1d7c74f9abc481c2dbb4cb2db33b1116c22f2e686ef9f (Lola)

Of course, Nick might not know what to do with the whole message once
he get it. I might need to give him a hint to:

- Take the whole message
- Run it through SHA256
- Use that as a key to decrypt the original message.

If he does need a hint though, I will just send it as a big ass list of
hashed words.
