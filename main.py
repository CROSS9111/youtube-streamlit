import streamlit as st
#import numpy as np
#import pandas as pd
#from PIL import Image
import time

st.title("hell")
st.write("プログレスバーの表示")
"Start!"
latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration{i+1}')
    bar.progress(i+1)
    time.sleep(0.1)
#fsutorinngu
left_column, right_column = st.columns(2)

button = left_column.button("右カラムを出現")
if button:
    right_column.write("ここは右カラム")

expander = st.expander("問い合わせ")
expander.write("問い合わせ回答1")
expander1 = st.expander("問い合わせ")
expander1.write("問い合わせ回答2")
expander2 = st.expander("問い合わせ")
expander2.write("問い合わせ回答3")

# text = st.text_input(2#     "3"たの趣味を教えてください"
# )
# "あなたの好きな数字は3"text,"です"

# condition = st.slider("あなたの調子は？",0,100,50)
# "あなたの調子は",condition,"です"


# option = st.selectbox(
#     "あなたの好きな数字を教えてください",
#     list(range(1,11))
# )
#"あなたの好きな数字は",option,"です"

# if st.checkbox("Show Image"):
#     img = Image.open("/Users/ada/Desktop/スクリーンショット 2023-03-09 19.53.36.png") 
#     st.image(img,caption="tekito",use_column_width=True)

# df = pd.DataFrame(
#         np.random.rand(100,2)/[50,50]+[35.69,139.70],
#         columns = ["lat","lon"]
#     )
# st.map(df)
#st.write(df)
#st.dataframe(df.style.highlight_max(axis=0),width=100,height=100)



"""
# 章
## 節
### 項

```python
import streamlit as st
import numpy as np
import pandas as pd
```
"""