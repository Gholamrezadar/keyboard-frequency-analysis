# Keyboard Frequency Analysis

Heatmaps for QWERTY and Persian standard keyboard layouts

Includes code for drawing a keyboard using matplotlib

Frequency data is available as csv files: `english_alphabet_freq.csv`, `persian_alphabet_freq.csv`

## Heatmaps

![QWERTY](QWERTY_keyboard_frequency_analysis.png)
![QWERTY](Persian_keyboard_frequency_analysis.png)

## Heatmaps - Contrasty

![QWERTY](QWERTY_keyboard_frequency_analysis_contrasty.png)
![QWERTY](Persian_keyboard_frequency_analysis_contrasty.png)

## Keyboards

![QWERTY](QWERTY_keyboard_raw.png)
![QWERTY](Persian_keyboard_raw.png)

## Update - Word Quality

You can calculate the typeability of a word using the `word_quality.py` script.

Maximum word quality is `5`.

### Rules

- Each finger is assigned a number from `1` to `8` (starting from the left pinky to the right pinky)
- Fingers have different weights:
  ```python
  finger_weights = {
        1: 1,
        2: 3,
        3: 3.5,
        4: 5,
        5: 5,
        6: 3.5,
        7: 3,
        8: 1,
    }
    ```
- Using a Finger twice in a row penalizes the word quality by (`6`-`finger_weight`)
  - So using finger #4 twice in a row penalizes the word quality by `6-5`=`1`
  - And using finger #1 twice in a row penalizes the word quality by `6-1`=`5`

### Usage

```bash
echo -e "1\ngholamrezadar" | python word_quality.py
```

Or just run the script and enter the word when prompted.

Example output:

```text
> Word: gholamrezadar

> Quality: 2.6153846153846154

> Finger usage:
1 : 4 [a z a a]
4 : 3 [g r r]
3 : 2 [e d]
5 : 2 [h m]
7 : 2 [o l]
2 : 0 []
6 : 0 []
8 : 0 []

> Double finger usage:
1 : 1
7 : 1
2 : 0
3 : 0
4 : 0
5 : 0
6 : 0
8 : 0
```

```text
> Word: fjfjfjfjfj
> Quality:  5.000

> Finger usage:
4 : 5 [f f f f f]
5 : 5 [j j j j j]
1 : 0 []
2 : 0 []
3 : 0 []
6 : 0 []
7 : 0 []
8 : 0 []

> Double finger usage:
1 : 0
2 : 0
3 : 0
4 : 0
5 : 0
6 : 0
7 : 0
8 : 0
```

> Note: Persian Layout not implemented yet.

## Update 2 - Word Quality Batch

### Usage

```bash
python word_quality_batch.py microsoft ebay instagram google facebook gholamrezadar amazon apple
```

Output:

```text
 3.888889: microsoft
 3.625000: ebay
 3.611111: instagram
 3.250000: google
 2.750000: facebook
 2.615385: gholamrezadar
 1.833333: amazon
 0.900000: apple
 ```
