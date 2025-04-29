import streamlit as st

#  Modular Render Functions 

def render_statistics_notes():
    st.header("STATISTICS NOTES")
    st.header("Module 1")
    st.markdown("---")
    st.header("Classifying Samples 🧪")
    
    st.markdown("""
    In statistics, different sampling methods are used to ensure that the data collected is representative of the population.
    The table below compares several common types of sampling methods.
    """)

    #st.image("mnt/data/89aa33b7-6efc-4617-89b9-220a656f1e91.png", caption="Types of Samples in Statistics", use_column_width=True)

    st.markdown("---")
    st.markdown("""
    ### 🔍 Types of Samples

    ---

    ### 🔹 Random sample
    - A sample of a predetermined size is chosen from the population.
    - Care is taken to choose the sample in such a way that **every sample of that size is equally likely to be selected**.
    - For example, a random sample can be chosen like this:  
    First, each member of the population is assigned a different number.  
    Then, a predetermined number of these assigned numbers is drawn at random using a computer program or a random number table.  
    The members assigned to the numbers drawn are selected for the sample.
    - A random sample with this description is also called a **simple random sample**.

    ---

    ### 🔹 Systematic sample
    - The members of the population are listed in some order.
    - Then, **every kᵗʰ member** (such as every 4ᵗʰ member) is selected for the sample until a predetermined sample size is reached.
    - *(The number k is usually chosen to be greater than 1 and small enough so that the predetermined sample size can be reached before the end of the list.)*

    ---

    ### 🔹 Stratified sample
    - The population is divided into groups, with each group made up of members that share some particular characteristic(s), such as an occupation.
    - Then, a **fixed number of members** (but not all members) **from each group are randomly selected** for the sample.

    ---

    ### 🔹 Cluster sample
    - The population is divided into groups that tend to exist naturally, such as cities in a state.
    - Then, **all members of some randomly chosen groups** (but not all groups) are selected for the sample.

    ---

    ### 🔹 Convenience sample
    - Members of a population that are **easily accessible** are selected for the sample.
    - No consideration is made for selecting randomly at any point during the selection process.
        """)

    # histogram stuff
    st.header("Grouped data 🧪")
    st.markdown("""
### 🔗 Online Calculator Resources

When dealing with grouped data problems (mean, median, mode, frequency tables, histograms), you can quickly use these calculators:

- 👉 [Frequency Distribution Calculator (Mean, Median, Mode)](https://www.socscistatistics.com/descriptive/frequencydistribution/default.aspx)
    The calculator will also spit out a number of other descriptors of your data - mean, median, skewness, and so on.
- 👉 [Online Mean, Median, and Mode Calculator From a Frequency Table](https://stats.libretexts.org/Learning_Objects/02%3A_Interactive_Statistics/05%3A_Online_Mean_Median_and_Mode_Calculator_From_a_Frequency_Table)
    Enter the lower bounds, the upper bounds, and the frequencies for each of the intervals of the frequency table and then hit Calculate.
- 👉 [Sample Variance, Standard deviation and coefficient of variation calculator for grouped data](https://atozmath.com/StatsG.aspx?q=4)

Frequency distribution problems: youll either be given class intervals, or a dataset with number of classes

Given number of classes, use this calculator:
- 👉 [Grouped Frequency Distribution Calculator](https://goodcalculators.com/grouped-frequency-distribution-calculator/)
Note that this is frequency, NOT cumulative frequency


---
""")

    st.header("Ogives 🧪")

    st.markdown("""
### 🔍 Ogive: Overview

- An **ogive** is a graph that represents the **cumulative relative frequencies** for the classes in a relative frequency distribution.
- The **upper class boundaries** are represented on the **horizontal axis**.

---

### 📚 Frequency Table

| Class Boundaries | Frequency | Relative Frequency |
|:-----------------|:----------|:-------------------|
| 20.5 – 24.5 | 7 | 0.250 |
| 24.5 – 28.5 | 8 | 0.286 |
| 28.5 – 32.5 | 4 | 0.143 |
| 32.5 – 36.5 | 4 | 0.143 |
| 36.5 – 40.5 | 3 | 0.107 |
| 40.5 – 44.5 | 2 | 0.071 |
| 44.5 – 48.5 | 0 | 0.000 |

Total frequency = 28  
Total relative frequency = 1.000

---

### 📈 Cumulative Relative Frequency Table

| Upper Class Boundary | Cumulative Relative Frequency |
|:---------------------|:------------------------------|
| Less than 20.5 | 0.000 |
| Less than 24.5 | 0.250 |
| Less than 28.5 | 0.536 |
| Less than 32.5 | 0.679 |
| Less than 36.5 | 0.821 |
| Less than 40.5 | 0.929 |
| Less than 44.5 | 1.000 |
| Less than 48.5 | 1.000 |

---

### 🧠 Important Notes
- An ogive **starts at 0** cumulative frequency.
- It is **always rising** (never decreases).
- Useful for finding medians, quartiles, percentiles.

---
    """)

    st.subheader("🧠 Manual Overview (if needed)")

    st.markdown("**Mean for grouped data:**")
    st.latex(r"\text{Mean} = \frac{\sum (f \times x)}{\sum f}")

    st.markdown("""
where:  
- \( f \) = frequency  
- \( x \) = midpoint of the class
""")

    st.markdown("**Median for grouped data:**")
    st.latex(r"\text{Median} = L + \left( \frac{\frac{n}{2} - F}{f_m} \right) \times w")

    st.markdown("""
where:  
- \( L \) = lower class boundary of the median class  
- \( n \) = total number of frequencies  
- \( F \) = cumulative frequency before the median class  
- \( f_m \) = frequency of the median class  
- \( w \) = class width
""")

    st.markdown("**Histogram basics:**")
    st.markdown("""
- x-axis = class boundaries  
- y-axis = frequencies  
- contiguous vertical bars
""")

    st.markdown("**Standard Deviation:**")
    st.markdown("Use grouped data SD formula, or plug values into a calculator.")

    st.markdown("---")

    st.subheader("⚡ Strategy")
    st.markdown("""
- **Use calculators whenever possible** to save time.
- **Know basic formulas** only for backup in case calculators are not allowed.
    """)

    st.header("Skewness of Distributions 🧠")

    st.markdown("""
### 🔍 How to Tell Skewness Quickly

---

Skewness as per Karl Pearson's Measure
**Skewness = Mean - Mode**

![Skewdness examples](https://media.geeksforgeeks.org/wp-content/uploads/20231101173636/Skewness-copy.webp)

### ➡️ Positively Skewed (Right-Skewed)
- Tail **stretches to the right** (toward larger numbers).
- Most data is **bunched on the left**, few larger outliers pull the mean to the right.
- **Mean > Median > Mode**.

**🔎 Look for:**
- Short bars on the right side.
- A few very large values.



---

### ⬅️ Negatively Skewed (Left-Skewed)
- Tail **stretches to the left** (toward smaller numbers).
- Most data is **bunched on the right**, few smaller outliers pull the mean to the left.
- **Mean < Median < Mode**.

**🔎 Look for:**
- Short bars on the left side.
- A few very small values.

---

### 🟰 Symmetric (Fairly Symmetric)
- Data is **evenly distributed** around the center.
- **Mean ≈ Median**.
- No obvious tails.

**🔎 Look for:**
- Balanced peak in the middle.

![Symmetric Distribution Example](https://upload.wikimedia.org/wikipedia/commons/thumb/9/9e/Normal_distribution_pdf.svg/320px-Normal_distribution_pdf.svg.png)

---

### 🧠 Super Fast Tip:
> - **Tail points = Skew points.**  
> (Tail goes right → positive skew; tail goes left → negative skew)

---

### ⚡ Strategy
When unsure:
- Find where the **long tail** is — even if it’s subtle.
- Remember, a few extreme values can cause **positive** or **negative** skew even if the rest looks "balanced."

---
    """)

    st.header("Module 2")
    st.markdown("---")

    st.markdown("""
    Measures of central tendency

    [this calculator is your friend](https://www.calculator.net/statistics-calculator.html)
    """)

    pass

def render_statistics_formulas():
    st.header("Statistics Formula Sheet")
    # TODO add statistics formulas here
    # TODO external calculator links if useful
    pass

def render_probability_notes():
    st.markdown("""
    ### ➡️ Mutually Exclusive (Disjoint) Events

    - Two events are **mutually exclusive** if they **cannot happen at the same time**.

    - **Formula:**
    """)
    st.latex(r"P(A \text{ or } B) = P(A) + P(B)")
    st.markdown("""
    - If
    """)
    st.latex(r"P(A \text{ and } B) \neq 0")
    st.markdown("""
    then **A and B are NOT mutually exclusive**.

    ✅ **Check:**
    - Find P(A  and  B).
    - If it's **not zero**, the events are **NOT mutually exclusive**.

    ---
    ### ➡️ Independent Events

    - Two events are **independent** if the occurrence of one **does not affect** the probability of the other.

    - **Formula:**
    """)
    st.latex(r"P(A \text{ and } B) = P(A) \times P(B)")
    st.markdown("""
    - If the equality **does not hold**, the events are **NOT independent**.

    ✅ **Check:**
    - Multiply P(A) * P(B).
    - Compare to the given  P(A and  B).
    """)

    st.markdown("---")

    st.markdown("## 🎯 Binomial Distribution - Central Tendency")

    st.markdown("""
    [Binominal Central distribution calculator](https://www.omnicalculator.com/statistics/binomial-distribution)

    [This one solves binomial probability and central tendency](https://www.emathhelp.net/calculators/probability-statistics/binomial-distribution-calculator/?n=9&x=4&p=0.13)
        helpful for questions such as:
        "Job Elimination In the past year, 13%  of businesses have eliminated jobs. If 9 businesses are selected at random, find the probability that at least 4 have eliminated jobs during the last year. Round the answer to at least four decimal places."

    [Multinominal probability calculator](https://stattrek.com/online-calculator/multinomial)  
        According to Mendel's theory, if tall and colorful plants are crossed with short and colorless plants, the corresponding probabilities are 9/16 for tall and colorful, 3/16 for tall and colorless, 3/16 for short and colorful, and 1/16 for short and colorless. If 7 plants are selected, find the probability that 3 will be tall and colorful, 2 will be tall and colorless, 2 will be short and colorful, and 0 will be short and colorless. Enter your answer as a simplified fraction or a decimal rounded to at least four decimal places.
    """)

    st.markdown("""
    The mean, variance, and standard deviation for a binomial distribution can be found using the following formulas:
    """)

    # Formulas
    st.latex(r"\mu = n \times p")
    st.latex(r"\sigma^2 = n \times p \times q")
    st.latex(r"\sigma = \sqrt{n \times p \times q}")

    st.markdown("""
    Where:
    - \( n \) = number of trials
    - \( p \) = probability of success
    - \( q = 1 - p \) = probability of failure

    ---
    """)

    st.markdown("### 🧠 Strategy")

    st.markdown("""
    - Step 1: Find \( p \) (probability of success).
    - Step 2: Find \( q = 1 - p \) (probability of failure).
    - Step 3: Calculate:
    """)

    st.latex(r"\text{Mean: } \mu = n \times p")
    st.latex(r"\text{Variance: } \sigma^2 = n \times p \times q")
    st.latex(r"\text{Standard Deviation: } \sigma = \sqrt{n \times p \times q}")

    st.markdown("""
    ✅ **Round final answers to at least one decimal place unless instructed otherwise.**
    """)

    
    st.markdown("""
    ### ⚡ Quick Mental Map

    | Find | Formula |
    |:----|:--------|
    | Mean | Multiply \( n \times p \) |
    | Variance | Multiply \( n \times p \times q \) |
    | Standard Deviation | Square root the variance |

    ---

    ### ✍️ Tiny Example

    Given:
    - \( n = 210 \)
    - \( p = 0.24 \)
    - \( q = 1 - 0.24 = 0.76 \)

    Then:
    """)

    st.latex(r"\mu = 210 \times 0.24 = 50.4")
    st.latex(r"\sigma^2 = 210 \times 0.24 \times 0.76 = 38.304")
    st.latex(r"\sigma = \sqrt{38.304} \approx 6.19")

    st.markdown("""
    ✅ Final Answers:
    - Mean ≈ 50.4
    - Variance ≈ 38.3
    - Standard Deviation ≈ 6.2

    ---
    """)

    pass

def render_probability_formulas():
    st.header("Probability Formula Sheet")
    # Add your probability formulas here
    # You can also add external links to calculators if needed
    
    pass



# --- Main App ---

st.markdown("# 📚 Probability and Statistics Exam Survival Guide")

# Four Main Tabs
tab_stats_notes, tab_stats_formulas, tab_prob_notes, tab_prob_formulas  = st.tabs([ 
    "📊 Statistics Notes", 
    "🧾 Statistics Formulas",
    "🧮 Probability Notes", 
    "🧾 Probability Formulas"
])

# Attach Render Functions
with tab_prob_notes:
    render_probability_notes()

with tab_prob_formulas:
    render_probability_formulas()

with tab_stats_notes:
    render_statistics_notes()

with tab_stats_formulas:
    render_statistics_formulas()
