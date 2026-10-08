import streamlit as st
import pandas as pd
import joblib


# =========================================================
# LOAD MODEL
# =========================================================

model = joblib.load("models/best_model.pkl")


# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="AttriSense AI",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)


# =========================================================
# SESSION STATE
# =========================================================

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "history" not in st.session_state:
    st.session_state.history = []


# =========================================================
# CUSTOM CSS
# =========================================================

st.markdown("""
<style>

.block-container {
    padding-top: 2rem;
    padding-bottom: 2rem;
}

/* Main headings */

.hero-title {
    font-size: 52px;
    font-weight: 800;
    margin-bottom: 5px;
}

.hero-subtitle {
    font-size: 20px;
    color: #6b7280;
    margin-bottom: 25px;
}

.section-title {
    font-size: 28px;
    font-weight: 700;
    margin-top: 15px;
    margin-bottom: 15px;
}

/* Login box */

.login-box {
    padding: 35px;
    border-radius: 20px;
    border: 1px solid #e5e7eb;
    background: #ffffff;
}

/* Cards */

.feature-card {
    padding: 25px;
    border-radius: 16px;
    border: 1px solid #e5e7eb;
    background: #f8fafc;
    min-height: 160px;
}

.feature-title {
    font-size: 20px;
    font-weight: 700;
}

.feature-text {
    color: #6b7280;
}

/* Dashboard cards */

.dashboard-card {
    padding: 20px;
    border-radius: 15px;
    background: #f8fafc;
    border: 1px solid #e5e7eb;
}

/* Risk */

.risk-high {
    padding: 25px;
    border-radius: 15px;
    text-align: center;
    background: #fee2e2;
}

.risk-low {
    padding: 25px;
    border-radius: 15px;
    text-align: center;
    background: #dcfce7;
}

/* Small text */

.small-text {
    color: #6b7280;
    font-size: 14px;
}

</style>
""", unsafe_allow_html=True)


# =========================================================
# LOGIN / LANDING PAGE
# =========================================================

if not st.session_state.logged_in:

    # Top branding
    st.markdown(
        '<div class="hero-title">🤖 AttriSense AI</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="hero-subtitle">'
        'Intelligent Employee Attrition Prediction & Analytics Platform'
        '</div>',
        unsafe_allow_html=True
    )

    st.divider()

    left, right = st.columns([1.4, 1])

    # -----------------------------------------------------
    # LEFT SIDE
    # -----------------------------------------------------

    with left:

        st.markdown(
            "## Predict. Analyze. Retain."
        )

        st.write(
            """
            AttriSense AI uses machine learning to identify employees
            who may be at risk of leaving an organization.
            
            Make data-driven decisions and understand employee
            attrition patterns using machine learning.
            """
        )

        st.write("### ✨ Platform Features")

        f1, f2 = st.columns(2)

        with f1:

            st.markdown("""
            <div class="feature-card">

            <div class="feature-title">
            🔮 Smart Prediction
            </div>

            <p class="feature-text">
            Predict whether an employee is likely to stay
            or leave the organization.
            </p>

            </div>
            """, unsafe_allow_html=True)

            st.write("")

            st.markdown("""
            <div class="feature-card">

            <div class="feature-title">
            📈 Model Analytics
            </div>

            <p class="feature-text">
            Compare machine learning models using
            accuracy, precision, recall and F1 score.
            </p>

            </div>
            """, unsafe_allow_html=True)

        with f2:

            st.markdown("""
            <div class="feature-card">

            <div class="feature-title">
            ⚠️ Risk Detection
            </div>

            <p class="feature-text">
            View attrition probability and identify
            employees with higher risk.
            </p>

            </div>
            """, unsafe_allow_html=True)

            st.write("")

            st.markdown("""
            <div class="feature-card">

            <div class="feature-title">
            📋 Prediction History
            </div>

            <p class="feature-text">
            Track predictions made during the current
            analysis session.
            </p>

            </div>
            """, unsafe_allow_html=True)

    # -----------------------------------------------------
    # RIGHT SIDE - LOGIN
    # -----------------------------------------------------

    with right:

        st.markdown("## 🔐 Welcome Back")

        st.write(
            "Login to access the employee analytics dashboard."
        )

        st.write("")

        username = st.text_input(
            "Username",
            placeholder="Enter username"
        )

        password = st.text_input(
            "Password",
            type="password",
            placeholder="Enter password"
        )

        st.write("")

        if st.button(
            "🚀 Login to Dashboard",
            use_container_width=True
        ):

            # Demo credentials
            if username == "admin" and password == "admin123":

                st.session_state.logged_in = True

                st.rerun()

            else:

                st.error(
                    "Invalid username or password."
                )

        st.write("")

        st.info(
            "Demo Login\n\n"
            "Username: admin\n\n"
            "Password: admin123"
        )

    st.divider()

    # Platform statistics

    st.markdown("### 📊 Platform Overview")

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.metric(
            "Employees",
            "1,470"
        )

    with c2:
        st.metric(
            "ML Models",
            "3"
        )

    with c3:
        st.metric(
            "Best Accuracy",
            "86.05%"
        )

    with c4:
        st.metric(
            "Best Model",
            "Logistic Regression"
        )

    st.stop()


# =========================================================
# SIDEBAR AFTER LOGIN
# =========================================================

with st.sidebar:

    st.markdown("## 🤖 AttriSense AI")

    st.caption(
        "Employee Intelligence Platform"
    )

    st.divider()

    page = st.radio(
        "Navigation",
        [
            "🏠 Dashboard",
            "🔮 Attrition Prediction",
            "📊 Analytics",
            "📋 Prediction History",
            "ℹ️ About Project"
        ]
    )

    st.divider()

    st.success(
        "🟢 Model Online"
    )

    st.caption(
        "Logistic Regression"
    )

    if st.button(
        "🚪 Logout",
        use_container_width=True
    ):

        st.session_state.logged_in = False

        st.rerun()


# =========================================================
# DASHBOARD
# =========================================================

if page == "🏠 Dashboard":

    st.markdown(
        '<div class="hero-title">Good to see you 👋</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="hero-subtitle">'
        'Employee Attrition Intelligence Dashboard'
        '</div>',
        unsafe_allow_html=True
    )

    # Statistics

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.metric(
            "Total Employees",
            "1,470"
        )

    with c2:
        st.metric(
            "Employees Left",
            "237"
        )

    with c3:
        st.metric(
            "Attrition Rate",
            "16.12%"
        )

    with c4:
        st.metric(
            "Model Accuracy",
            "86.05%"
        )

    st.divider()

    # Dataset overview

    left, right = st.columns(2)

    with left:

        st.subheader("📊 Attrition Overview")

        attrition_data = pd.DataFrame({
            "Status": [
                "Stayed",
                "Left"
            ],
            "Employees": [
                1233,
                237
            ]
        })

        st.bar_chart(
            attrition_data.set_index("Status")
        )

    with right:

        st.subheader("🤖 Model Summary")

        st.success(
            "Best Model: Logistic Regression"
        )

        st.write(
            "The final model was selected based on "
            "the highest F1 Score."
        )

        st.metric(
            "F1 Score",
            "43.84%"
        )

        st.metric(
            "Precision",
            "61.54%"
        )

    st.divider()

    st.info(
        "💡 Use the Attrition Prediction section to "
        "analyze an individual employee."
    )


# =========================================================
# ATTRITION PREDICTION
# =========================================================

elif page == "🔮 Attrition Prediction":

    st.title("🔮 Employee Attrition Prediction")

    st.write(
        "Enter employee information to generate an AI-based "
        "attrition prediction."
    )

    st.divider()

    st.subheader("👤 Employee Information")

    col1, col2, col3 = st.columns(3)

    # Column 1

    with col1:

        age = st.number_input(
            "Age",
            18,
            60,
            30
        )

        business_travel = st.selectbox(
            "Business Travel",
            [
                "Travel_Rarely",
                "Travel_Frequently",
                "Non-Travel"
            ]
        )

        department = st.selectbox(
            "Department",
            [
                "Sales",
                "Research & Development",
                "Human Resources"
            ]
        )

        education = st.number_input(
            "Education Level",
            1,
            5,
            3
        )

        education_field = st.selectbox(
            "Education Field",
            [
                "Life Sciences",
                "Medical",
                "Marketing",
                "Technical Degree",
                "Human Resources",
                "Other"
            ]
        )

    # Column 2

    with col2:

        gender = st.selectbox(
            "Gender",
            ["Male", "Female"]
        )

        job_role = st.selectbox(
            "Job Role",
            [
                "Sales Executive",
                "Research Scientist",
                "Laboratory Technician",
                "Manufacturing Director",
                "Healthcare Representative",
                "Manager",
                "Sales Representative",
                "Research Director",
                "Human Resources"
            ]
        )

        marital_status = st.selectbox(
            "Marital Status",
            [
                "Single",
                "Married",
                "Divorced"
            ]
        )

        job_level = st.number_input(
            "Job Level",
            1,
            5,
            2
        )

        job_satisfaction = st.number_input(
            "Job Satisfaction",
            1,
            4,
            3
        )

    # Column 3

    with col3:

        monthly_income = st.number_input(
            "Monthly Income",
            1000,
            20000,
            5000
        )

        overtime = st.selectbox(
            "OverTime",
            ["Yes", "No"]
        )

        total_working_years = st.number_input(
            "Total Working Years",
            0,
            40,
            5
        )

        years_at_company = st.number_input(
            "Years at Company",
            0,
            40,
            3
        )

        years_in_current_role = st.number_input(
            "Years in Current Role",
            0,
            20,
            2
        )

    st.divider()

    if st.button(
        "🔮 ANALYZE EMPLOYEE",
        use_container_width=True
    ):

        input_data = pd.DataFrame({

            "Age": [age],
            "BusinessTravel": [business_travel],
            "Department": [department],
            "DistanceFromHome": [10],
            "Education": [education],
            "EducationField": [education_field],
            "EnvironmentSatisfaction": [3],
            "Gender": [gender],
            "HourlyRate": [65],
            "JobInvolvement": [3],
            "JobLevel": [job_level],
            "JobRole": [job_role],
            "JobSatisfaction": [job_satisfaction],
            "MaritalStatus": [marital_status],
            "MonthlyIncome": [monthly_income],
            "MonthlyRate": [15000],
            "NumCompaniesWorked": [2],
            "OverTime": [overtime],
            "PercentSalaryHike": [15],
            "PerformanceRating": [3],
            "RelationshipSatisfaction": [3],
            "StockOptionLevel": [1],
            "TotalWorkingYears": [total_working_years],
            "TrainingTimesLastYear": [3],
            "WorkLifeBalance": [3],
            "YearsAtCompany": [years_at_company],
            "YearsInCurrentRole": [years_in_current_role],
            "YearsSinceLastPromotion": [1],
            "YearsWithCurrManager": [2],
            "DailyRate": [800]
        })

        prediction = model.predict(input_data)[0]

        probability = model.predict_proba(
            input_data
        )[0][1]

        probability_percent = probability * 100

        # Risk level

        if probability_percent >= 60:

            risk = "High Risk"

        elif probability_percent >= 30:

            risk = "Medium Risk"

        else:

            risk = "Low Risk"

        # Save history

        result = (
            "Likely to Leave"
            if prediction == 1
            else "Likely to Stay"
        )

        st.session_state.history.append({

            "Age": age,
            "Job Role": job_role,
            "Department": department,
            "Probability": f"{probability_percent:.2f}%",
            "Risk": risk,
            "Prediction": result
        })

        st.divider()

        st.subheader("🎯 AI Analysis Result")

        if prediction == 1:

            st.error(
                "🔴 Employee is likely to leave the organization."
            )

        else:

            st.success(
                "🟢 Employee is likely to stay in the organization."
            )

        c1, c2, c3 = st.columns(3)

        with c1:

            st.metric(
                "Attrition Probability",
                f"{probability_percent:.2f}%"
            )

        with c2:

            st.metric(
                "Risk Level",
                risk
            )

        with c3:

            st.metric(
                "Prediction",
                result
            )

        st.write("### 📈 Attrition Risk Score")

        st.progress(
            float(probability)
        )

        st.caption(
            "Higher score indicates a higher predicted probability "
            "of employee attrition."
        )

        st.subheader("📋 Employee Summary")

        summary = pd.DataFrame({

            "Attribute": [
                "Age",
                "Department",
                "Job Role",
                "Job Level",
                "Job Satisfaction",
                "Monthly Income",
                "Overtime",
                "Years at Company"
            ],

            "Value": [
                age,
                department,
                job_role,
                job_level,
                job_satisfaction,
                monthly_income,
                overtime,
                years_at_company
            ]
        })

        st.dataframe(
            summary,
            use_container_width=True,
            hide_index=True
        )

        st.info(
            "ℹ️ Some additional dataset features use default "
            "values in this simplified interface."
        )


# =========================================================
# ANALYTICS
# =========================================================

elif page == "📊 Analytics":

    st.title("📊 Analytics & Model Performance")

    st.write(
        "Explore the dataset and compare machine learning models."
    )

    st.divider()

    # Attrition data

    col1, col2 = st.columns(2)

    with col1:

        st.subheader("Employee Attrition")

        attrition = pd.DataFrame({

            "Status": [
                "Stayed",
                "Left"
            ],

            "Employees": [
                1233,
                237
            ]
        })

        st.bar_chart(
            attrition.set_index("Status")
        )

    with col2:

        st.subheader("Model Performance")

        performance = pd.DataFrame({

            "Model": [
                "Logistic Regression",
                "Decision Tree",
                "Random Forest"
            ],

            "Accuracy": [
                86.05,
                76.53,
                85.03
            ],

            "Precision": [
                61.54,
                31.03,
                63.64
            ],

            "Recall": [
                34.04,
                38.30,
                14.89
            ],

            "F1 Score": [
                43.84,
                34.29,
                24.14
            ]
        })

        st.bar_chart(
            performance.set_index("Model")
        )

    st.divider()

    st.subheader("🏆 Model Comparison")

    st.dataframe(
        performance,
        use_container_width=True,
        hide_index=True
    )

    st.success(
        "Logistic Regression achieved the highest F1 Score "
        "and was selected as the final model."
    )


# =========================================================
# HISTORY
# =========================================================

elif page == "📋 Prediction History":

    st.title("📋 Prediction History")

    if len(st.session_state.history) == 0:

        st.info(
            "No predictions have been made yet."
        )

        st.write(
            "Go to **Attrition Prediction** and analyze an employee."
        )

    else:

        history_df = pd.DataFrame(
            st.session_state.history
        )

        st.dataframe(
            history_df,
            use_container_width=True,
            hide_index=True
        )

        st.metric(
            "Total Predictions",
            len(st.session_state.history)
        )


# =========================================================
# ABOUT
# =========================================================

elif page == "ℹ️ About Project":

    st.title("ℹ️ About AttriSense AI")

    st.write(
        """
        ### Employee Attrition Prediction Using Machine Learning

        AttriSense AI is a machine learning based platform designed
        to predict employee attrition.

        The system evaluates employee information and predicts
        whether an employee is likely to stay or leave.
        """
    )

    st.divider()

    st.subheader("🔄 Machine Learning Workflow")

    st.write(
        """
        📂 Dataset
        ↓
        
        🧹 Data Preprocessing
        ↓
        
        ✂️ Train-Test Split
        ↓
        
        🤖 Model Training
        ↓
        
        📊 Model Comparison
        ↓
        
        🏆 Best Model Selection
        ↓
        
        🔮 Employee Prediction
        """
    )

    st.divider()

    st.subheader("🤖 Algorithms Used")

    st.write(
        """
        • Logistic Regression  
        • Decision Tree  
        • Random Forest
        """
    )

    st.subheader("🏆 Final Model")

    st.success(
        "Logistic Regression — 86.05% Accuracy"
    )

    st.subheader("📊 Dataset")

    st.write(
        "IBM HR Analytics Employee Attrition & Performance Dataset"
    )

    st.write(
        "Records: 1,470 | Features used: 30"
    )

    st.caption(
        "This platform is developed as an academic machine learning project."
    )