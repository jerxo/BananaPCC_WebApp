import base64
import streamlit as st

st.set_page_config(page_title="Cavendish Banana Production Cost Calculator", layout="wide")

with open('style_bananacostcalculator.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

@st.cache_data
def get_img_as_base64(file):
    with open(file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()


img = get_img_as_base64("banana1.jpg")

page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] > .main {{
    background-image: url("data:image/png;base64,{img}");
    background-size: cover; /* This will cover the entire container without stretching */
    background-position: center center; /* Center the image horizontally and vertically */
    background-repeat: no-repeat; /* Prevent image from repeating */
    height: 100vh; /* Set the height to 100% of the viewport height (full height) */
}}
</style>
"""

st.markdown(page_bg_img, unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center'>Cavendish Banana Cost Calculator</h1>", unsafe_allow_html=True)
st.write("---")

bi_cost = 0
bs_cost = 0
fert_cost = 0
h_cost = 0
input_cost = 0

polybag_cost = 0
ribbons_cost = 0
twine_cost = 0
bamboo_cost = 0
materials_cost = 0

spraying_cost = 0
fertilizing_cost = 0
weeding_cost = 0
deleafing_cost = 0
bagging_cost = 0
harvesting_cost = 0
labor_cost = 0

transpo_cost = 0
packing_cost = 0
prodother_cost = 0

with st.expander("Cavendish Banana Farm General Information"):
	col1, col2 = st.columns(2)
	with col1:
		hectares = st.number_input("Number of hectares of your farm:", min_value=0.00, step=1.0)
		bunch = st.number_input("Number of banana bunch harvested:", min_value=0.00, step=1.0)

	with col2:
		dataset = st.radio("Please select the dataset to use for the computation:", ("Sto. Tomas, Davao del Norte - CHED 2017", "Sto. Tomas, Davao del Norte - World Bank 2012"))

maincol1, maincol2 = st.columns(2)
with maincol1:
	st.header("Production Costs")
	tab1, tab2, tab3, tab4 = st.tabs(["Input Costs", "Materials Costs", "Labor Costs", "Other Cost"])
	
	with tab1:
		if dataset == "Sto. Tomas, Davao del Norte - World Bank 2012":
			st.subheader("Bud Injection")
			bi_cost_per_liter = st.number_input("How much does a liter of Bud Injection cost?", min_value=0.00, step=1.0)
			bi_number_liter = st.number_input("How many liters of Bud Injection did you use per hectare?", min_value=0.00, step=1.0)
			bi_days = st.number_input("How many days in a week did you apply the Bud Injection?", min_value=0.00, max_value=7.00, step=1.0)
			bi_weeks = st.number_input("How many weeks in a month did you apply the Bud Injection?", min_value=0.00, max_value=4.00, step=1.0)
			bi_months = st.number_input("How many months in a year did you apply the Bud Injection?", min_value=0.00, max_value=12.00,  step=1.0)
			st.subheader("Bunch Spray")
			bs_cost_per_liter = st.number_input("How much does a liter of Bunch Spray cost?", min_value=0.00, step=1.0)
			bs_number_liter = st.number_input("How many liters of Bunch Spray did you use per hectare?", min_value=0.00, step=1.0)
			bs_days = st.number_input("How many days in a week did you apply the Bunch Spray?", min_value=0.00, max_value=7.00, step=1.0)
			bs_weeks = st.number_input("How many weeks in a month did you apply the Bunch Spray?", min_value=0.00, max_value=4.00, step=1.0)
			bs_months = st.number_input("How many months in a year did you apply the Bunch Spray?", min_value=0.00,  max_value=12.00, step=1.0)
			st.subheader("Herbicide")
			h_cost_per_liter = st.number_input("How much does a liter of Herbicide cost?", min_value=0.00, step=1.0)
			h_number_liter = st.number_input("How many liters of Herbicide did you use per hectare?", min_value=0.00, step=1.0)
			h_days = st.number_input("How many days in a week did you apply the Herbicide?", min_value=0.00, max_value=7.00, step=1.0)
			h_weeks = st.number_input("How many weeks in a month did you apply the Herbicide?", min_value=0.00, max_value=4.00, step=1.0)
			h_months = st.number_input("How many months in a year did you apply the Herbicide?", min_value=0.00,  max_value=12.00, step=1.0)
			st.subheader("Fertilizer")
			fert_cost_per_sackbag = st.number_input("How much does a sack/bag of Fertilizer cost?", min_value=0.00, step=1.0)
			fert_number_sackbag = st.number_input("How many sacks/bags of Fertilizer did you use per hectare?", min_value=0.00, step=1.0)
			fert_days = st.number_input("How many days in a week did you apply the Fertilizer?", min_value=0.00, max_value=7.00, step=1.0)
			fert_weeks = st.number_input("How many weeks in a month did you apply the Fertilizer?", min_value=0.00, max_value=4.00, step=1.0)
			fert_months = st.number_input("How many months in a year did you apply the Fertilizer?", min_value=0.00, max_value=12.00, step=1.0)
			st.subheader("Sigatoka Control Chemical")
			siga_cost_per_sackbag = st.number_input("How much does a liter of Sigatoka Control Chemical cost?", min_value=0.00, step=1.0)
			siga_number_sackbag = st.number_input("How many liters of Sigatoka Control Chemical did you use per hectare?", min_value=0.00, step=1.0)
			siga_days = st.number_input("How many days in a week did you apply the Sigatoka Control Chemical?", min_value=0.00, max_value=7.00, step=1.0)
			siga_weeks = st.number_input("How many weeks in a month did you apply the Sigatoka Control Chemical?", min_value=0.00, max_value=4.00, step=1.0)
			siga_months = st.number_input("How many months in a year did you apply the Sigatoka Control Chemical?", min_value=0.00, max_value=12.00, step=1.0)
		elif dataset == "Sto. Tomas, Davao del Norte - CHED 2017":
			st.subheader("Fertilizer")
			fert_cost_per_sackbag = st.number_input("How much does a sack/bag of Fertilizer cost?", min_value=0.00, step=1.0)
			fert_number_sackbag = st.number_input("How many sacks/bags of Fertilizer did you use per hectare?", min_value=0.00, step=1.0)
			fert_days = st.number_input("How many days in a week did you apply the Fertilizer?", min_value=0.00, max_value=7.00, step=1.0)
			fert_weeks = st.number_input("How many weeks in a month did you apply the Fertilizer?", min_value=0.00, max_value=4.00, step=1.0)
			fert_months = st.number_input("How many months in a year did you apply the Fertilizer?", min_value=0.00, max_value=12.00, step=1.0)
			st.subheader("Sigatoka Control Chemical")
			siga_cost_per_sackbag = st.number_input("How much does a liter of Sigatoka Control Chemical cost?", min_value=0.00, step=1.0)
			siga_number_sackbag = st.number_input("How many liters of Sigatoka Control Chemical did you use per hectare?", min_value=0.00, step=1.0)
			siga_days = st.number_input("How many days in a week did you apply the Sigatoka Control Chemical?", min_value=0.00, max_value=7.00, step=1.0)
			siga_weeks = st.number_input("How many weeks in a month did you apply the Sigatoka Control Chemical?", min_value=0.00, max_value=4.00, step=1.0)
			siga_months = st.number_input("How many months in a year did you apply the Sigatoka Control Chemical?", min_value=0.00, max_value=12.00, step=1.0)
	
	with tab2:
		st.subheader("Polybags")
		polybags_yesno = st.radio("Did you use polybags?", ("Yes", "No"))
		if polybags_yesno == "Yes":
			polybags_cost_per_kilo = st.number_input("How much does a kilogram of polybags cost?", min_value=0.00, step=1.0)
			polybags_number_kilo = st.number_input("How many kilograms of polybags did you use per hectare?", min_value=0.00, step=1.0)
		st.subheader("Ribbons")
		ribbons_yesno = st.radio("Did you use ribbons?", ("Yes", "No"))
		if ribbons_yesno == "Yes":
			ribbons_cost_per_kilo = st.number_input("How much does a kilogram of ribbons cost?", min_value=0.00, step=1.0)
			ribbons_number_kilo = st.number_input("How many kilograms of ribbons did you use per hectare?", min_value=0.00, step=1.0)
		st.subheader("Twine")
		twine_yesno = st.radio("Did you use twine?", ("Yes", "No"))
		if twine_yesno == "Yes":
			twine_cost_per_kilo = st.number_input("How much does a kilogram of twine cost?", min_value=0.00, step=1.0)
			twine_number_kilo = st.number_input("How many kilograms of twine did you use per hectare?", min_value=0.00, step=1.0)
		st.subheader("Bamboo")
		bamboo_yesno = st.radio("Did you use bamboo?", ("Yes", "No"))
		if bamboo_yesno == "Yes":
			bamboo_cost_per_piece = st.number_input("How much does a piece of bamboo cost?", min_value=0.00, step=1.0)
			bamboo_number_piece = st.number_input("How many pieces of bamboo did you use per hectare?", min_value=0.00, step=1.0)
		st.subheader("Fuel/Oil/Lubricants")
		fol_yesno = st.radio("Did you use Fuel/Oil/Lubricants?", ("Yes", "No"))
		if fol_yesno == "Yes":
			fol_cost_per_piece = st.number_input("How much does a liter of Fuel/Oil/Lubricants cost?", min_value=0.00, step=1.0)
			fol_number_piece = st.number_input("How many liters of Fuel/Oil/Lubricants did you use per hectare?", min_value=0.00, step=1.0)
			
	with tab3:
		if dataset == "Sto. Tomas, Davao del Norte - World Bank 2012":
			st.subheader("Deleafing")
			deleafing_yesno = st.radio("Did you incur any costs for deleafing?:", ("Yes", "No"))
			if deleafing_yesno == "Yes":
				deleafing_laborers = st.number_input("How many laborers did you hire for deleafing?", min_value=0.00, step=1.0)
				deleafing_days = st.number_input("How many days in a week do you perform deleafing?", min_value=0.00, max_value=7.00, step=1.0)
				deleafing_weeks = st.number_input("How many weeks in a month did you perform deleafing?", min_value=0.00, max_value=4.00, step=1.0)
				deleafing_months = st.number_input("How many months in a year did you perform deleafing?", min_value=0.00, max_value=12.00, step=1.0)
			st.subheader("Spraying")
			spraying_yesno = st.radio("Did you incur any costs for Spraying?:", ("Yes", "No"))
			if spraying_yesno == "Yes":
				spraying_laborers = st.number_input("How many laborers did you hire for spraying?", min_value=0.00, step=1.0)
				spraying_days = st.number_input("How many days in a week do you spray?", min_value=0.00, max_value=7.00, step=1.0)
				spraying_weeks = st.number_input("How many weeks in a month did you spray?", min_value=0.00, max_value=4.00, step=1.0)
				spraying_months = st.number_input("How many months in a year did you spray?", min_value=0.00, max_value=12.00, step=1.0)
			st.subheader("Fertilizing")
			fertilizing_yesno = st.radio("Did you incur any costs for Fertilizing?:", ("Yes", "No"))
			if fertilizing_yesno == "Yes":
				fertilizing_laborers = st.number_input("How many laborers did you hire for fertilizing?", min_value=0.00, step=1.0)
				fertilizing_days = st.number_input("How many days in a week do you fertilize?", min_value=0.00, max_value=7.00, step=1.0)
				fertilizing_weeks = st.number_input("How many weeks in a month did you fertilize?", min_value=0.00, max_value=4.00, step=1.0)
				fertilizing_months = st.number_input("How many months in a year did you fertilize?", min_value=0.00, max_value=12.00, step=1.0)
			st.subheader("Weeding")
			weeding_yesno = st.radio("Did you incur any costs for Weeding?:", ("Yes", "No"))
			if weeding_yesno == "Yes":
				weeding_laborers = st.number_input("How many laborers did you hire for Weeding?", min_value=0.00, step=1.0)
				weeding_days = st.number_input("How many days in a week do you perform weeding?", min_value=0.00, max_value=7.00, step=1.0)
				weeding_weeks = st.number_input("How many weeks in a month did you perform weeding?", min_value=0.00, max_value=4.00, step=1.0)
				weeding_months = st.number_input("How many months in a year did you perform weeding?", min_value=0.00, max_value=12.00, step=1.0)
			st.subheader("Bagging")
			bagging_yesno = st.radio("Did you incur any costs for bagging?:", ("Yes", "No"))
			if bagging_yesno == "Yes":
				bagging_laborers = st.number_input("How many laborers did you hire for bagging?", min_value=0.00, step=1.0)
				bagging_days = st.number_input("How many days in a week do you perform bagging?", min_value=0.00, max_value=7.00, step=1.0)
				bagging_weeks = st.number_input("How many weeks in a month did you perform bagging?", min_value=0.00, max_value=4.00, step=1.0)
				bagging_months = st.number_input("How many months in a year did you perform bagging?", min_value=0.00, max_value=12.00, step=1.0)
			st.subheader("Harvesting")
			harvesting_yesno = st.radio("Did you incur any costs for harvesting?:", ("Yes", "No"))
			if harvesting_yesno == "Yes":
				harvesting_cost_per_bunch = st.number_input("How much does each laborer get paid for harvesting one bunch?", min_value=0.00, step=1.0)
				
		elif dataset == "Sto. Tomas, Davao del Norte - CHED 2017":
			st.subheader("Spraying")
			spraying_yesno = st.radio("Did you incur any costs for Spraying?:", ("Yes", "No"))
			if spraying_yesno == "Yes":
				spraying_laborers = st.number_input("How many laborers did you hire for spraying?", min_value=0.00, step=1.0)
				spraying_days = st.number_input("How many days in a week do you spray?", min_value=0.00, max_value=7.00, step=1.0)
				spraying_weeks = st.number_input("How many weeks in a month did you spray?", min_value=0.00, max_value=4.00, step=1.0)
				spraying_months = st.number_input("How many months in a year did you spray?", min_value=0.00, max_value=12.00, step=1.0)
			st.subheader("Fertilizing")
			fertilizing_yesno = st.radio("Did you incur any costs for Fertilizing?:", ("Yes", "No"))
			if fertilizing_yesno == "Yes":
				fertilizing_laborers = st.number_input("How many laborers did you hire for fertilizing?", min_value=0.00, step=1.0)
				fertilizing_days = st.number_input("How many days in a week do you fertilize?", min_value=0.00, max_value=7.00, step=1.0)
				fertilizing_weeks = st.number_input("How many weeks in a month did you fertilize?", min_value=0.00, max_value=4.00, step=1.0)
				fertilizing_months = st.number_input("How many months in a year did you fertilize?", min_value=0.00, max_value=12.00, step=1.0)
			st.subheader("Weeding")
			weeding_yesno = st.radio("Did you incur any costs for Weeding?:", ("Yes", "No"))
			if weeding_yesno == "Yes":
				weeding_laborers = st.number_input("How many laborers did you hire for Weeding?", min_value=0.00, step=1.0)
				weeding_days = st.number_input("How many days in a week do you perform weeding?", min_value=0.00, max_value=7.00, step=1.0)
				weeding_weeks = st.number_input("How many weeks in a month did you perform weeding?", min_value=0.00, max_value=4.00, step=1.0)
				weeding_months = st.number_input("How many months in a year did you perform weeding?", min_value=0.00, max_value=12.00, step=1.0)
			st.subheader("Bagging")
			bagging_yesno = st.radio("Did you incur any costs for bagging?:", ("Yes", "No"))
			if bagging_yesno == "Yes":
				bagging_laborers = st.number_input("How many laborers did you hire for bagging?", min_value=0.00, step=1.0)
				bagging_days = st.number_input("How many days in a week do you perform bagging?", min_value=0.00, max_value=7.00, step=1.0)
				bagging_weeks = st.number_input("How many weeks in a month did you perform bagging?", min_value=0.00, max_value=4.00, step=1.0)
				bagging_months = st.number_input("How many months in a year did you perform bagging?", min_value=0.00, max_value=12.00, step=1.0)
			st.subheader("Harvesting")
			harvesting_yesno = st.radio("Did you incur any costs for harvesting?:", ("Yes", "No"))
			if harvesting_yesno == "Yes":
				harvesting_cost_per_bunch = st.number_input("How much does each laborer get paid for harvesting one bunch?", min_value=0.00, step=1.0)
    
	with tab4:
		prodother_cost = st.number_input(label="Enter total cost for unaccounted production items: ", min_value=0.00, step=10.00)

with maincol2:
	st.header("Post-Harvest Costs")
	tab1, tab2 = st.tabs(["Labor Costs", "Other Cost"])
	with tab1:
		st.subheader("Packing")
		packing_yesno = st.radio("Did you incur any costs for packing?:", ("Yes", "No"))
		if packing_yesno == "Yes":
			packing_laborers = st.number_input("How many laborers did you hire for packing?", min_value=0.00, step=1.0)
			packing_cost_per_laborer = st.number_input("How much does each laborer cost for packing?", min_value=0.00, step=1.0)
			packing_days = st.number_input("How many days in a week do you perform packing?", min_value=0.00, max_value=7.00, step=1.0)
			packing_weeks = st.number_input("How many weeks in a month did you perform packing?", min_value=0.00, max_value=4.00, step=1.0)
			packing_months = st.number_input("How many months in a year did you perform packing?", min_value=0.00, max_value=12.00, step=1.0)

	with tab2:
		st.subheader("Transportation")
		transpo_yesno = st.radio("Did you incur any costs for transportation?:", ("Yes", "No"))
		if transpo_yesno == "Yes":
			transpo_cost = st.number_input("How much did you spent on transportation?", min_value=0.00, step=1.0)

def calculate():
	if dataset == "Sto. Tomas, Davao del Norte - World Bank 2012":
		lb_deleafing_cost_per_laborer = 75
		m_deleafing_cost_per_laborer = 180
		ub_deleafing_cost_per_laborer = 180
		
		lb_spraying_cost_per_laborer = 180
		m_spraying_cost_per_laborer = 180
		ub_spraying_cost_per_laborer = 200
	
		lb_fertilizing_cost_per_laborer = 180
		m_fertilizing_cost_per_laborer = 200
		ub_fertilizing_cost_per_laborer = 200
	
		lb_weeding_cost_per_laborer = 180
		m_weeding_cost_per_laborer = 180
		ub_weeding_cost_per_laborer = 200
	
		lb_bagging_cost_per_laborer = 180
		m_bagging_cost_per_laborer = 180
		ub_bagging_cost_per_laborer = 200

		input_cost = 0
		materials_cost = 0
		lb_labor_cost = 0
		ub_labor_cost = 0
		lb_total_cost = 0
		ub_total_cost = 0
		
		bi_cost = (bi_cost_per_liter * bi_number_liter * bi_days * bi_weeks * bi_months)
		bs_cost = (bs_cost_per_liter * bs_number_liter * bs_days * bs_weeks * bs_months)
		fert_cost = (fert_cost_per_sackbag * fert_number_sackbag * fert_days * fert_weeks * fert_months)
		h_cost = (h_cost_per_liter * h_number_liter * h_days * h_weeks * h_months)
		siga_cost = (siga_cost_per_sackbag * siga_number_sackbag * siga_days * siga_weeks * siga_months)
		input_cost = (bi_cost + bs_cost + fert_cost + siga_cost + h_cost)
	
		polybag_cost = (polybags_cost_per_kilo * polybags_number_kilo)
		ribbons_cost = (ribbons_cost_per_kilo * ribbons_number_kilo)
		twine_cost = (twine_cost_per_kilo * twine_number_kilo)
		bamboo_cost = (bamboo_cost_per_piece * bamboo_number_piece)
		materials_cost = (polybag_cost + ribbons_cost + twine_cost + bamboo_cost)
	
		lb_spraying_cost = (spraying_laborers * lb_spraying_cost_per_laborer * spraying_days * spraying_weeks * spraying_months)
		lb_fertilizing_cost = (fertilizing_laborers * lb_fertilizing_cost_per_laborer * fertilizing_days * fertilizing_weeks * fertilizing_months)
		lb_weeding_cost = (weeding_laborers * lb_weeding_cost_per_laborer * weeding_days * weeding_weeks * weeding_months)
		lb_deleafing_cost = (deleafing_laborers * lb_deleafing_cost_per_laborer * deleafing_days * deleafing_weeks * deleafing_months)
		lb_bagging_cost = (bagging_laborers * lb_bagging_cost_per_laborer * bagging_days * bagging_weeks * bagging_months)

		m_spraying_cost = (spraying_laborers * m_spraying_cost_per_laborer * spraying_days * spraying_weeks * spraying_months)
		m_fertilizing_cost = (fertilizing_laborers * m_fertilizing_cost_per_laborer * fertilizing_days * fertilizing_weeks * fertilizing_months)
		m_weeding_cost = (weeding_laborers * m_weeding_cost_per_laborer * weeding_days * weeding_weeks * weeding_months)
		m_deleafing_cost = (deleafing_laborers * m_deleafing_cost_per_laborer * deleafing_days * deleafing_weeks * deleafing_months)
		m_bagging_cost = (bagging_laborers * m_bagging_cost_per_laborer * bagging_days * bagging_weeks * bagging_months)

		ub_spraying_cost = (spraying_laborers * ub_spraying_cost_per_laborer * spraying_days * spraying_weeks * spraying_months)
		ub_fertilizing_cost = (fertilizing_laborers * ub_fertilizing_cost_per_laborer * fertilizing_days * fertilizing_weeks * fertilizing_months)
		ub_weeding_cost = (weeding_laborers * ub_weeding_cost_per_laborer * weeding_days * weeding_weeks * weeding_months)
		ub_deleafing_cost = (deleafing_laborers * ub_deleafing_cost_per_laborer * deleafing_days * deleafing_weeks * deleafing_months)
		ub_bagging_cost = (bagging_laborers * ub_bagging_cost_per_laborer * bagging_days * bagging_weeks * bagging_months)

		packing_cost = packing_laborers * packing_cost_per_laborer * packing_days * packing_weeks * packing_months
		harvesting_cost = (harvesting_cost_per_bunch * bunch)
		lb_labor_cost = (lb_spraying_cost + lb_fertilizing_cost + lb_weeding_cost + lb_deleafing_cost + lb_bagging_cost + harvesting_cost + packing_cost)
		m_labor_cost = (m_spraying_cost + m_fertilizing_cost + m_weeding_cost + m_deleafing_cost + m_bagging_cost + harvesting_cost + packing_cost)
		ub_labor_cost = (ub_spraying_cost + ub_fertilizing_cost + ub_weeding_cost + ub_deleafing_cost + ub_bagging_cost + harvesting_cost + packing_cost)
	
		lb_total_cost = input_cost + materials_cost + lb_labor_cost + prodother_cost + transpo_cost
		ub_total_cost = input_cost + materials_cost + ub_labor_cost + prodother_cost + transpo_cost

		return input_cost, materials_cost, lb_labor_cost, ub_labor_cost, lb_total_cost, ub_total_cost
		
	elif dataset == "Sto. Tomas, Davao del Norte - CHED 2017":
		input_cost = 0
		materials_cost = 0
		total_cost = 0
		
		bi_cost = 0
		bs_cost = 0
		fert_cost = (fert_cost_per_sackbag * fert_number_sackbag * fert_days * fert_weeks * fert_months)
		siga_cost = (siga_cost_per_sackbag * siga_number_sackbag * siga_days * siga_weeks * siga_months)
		h_cost = 0
		input_cost = (fert_cost + siga_cost)
	
		polybag_cost = (polybags_cost_per_kilo * polybags_number_kilo)
		ribbons_cost = (ribbons_cost_per_kilo * ribbons_number_kilo)
		twine_cost = (twine_cost_per_kilo * twine_number_kilo)
		bamboo_cost = (bamboo_cost_per_piece * bamboo_number_piece)
		materials_cost = (polybag_cost + ribbons_cost + twine_cost + bamboo_cost)
	
		spraying_cost = (spraying_laborers * 340 * spraying_days * spraying_weeks * spraying_months)
		fertilizing_cost = (fertilizing_laborers * 340 * fertilizing_days * fertilizing_weeks * fertilizing_months)
		weeding_cost = (weeding_laborers * 340 * weeding_days * weeding_weeks * weeding_months)
		deleafing_cost = 0
		bagging_cost = (bagging_laborers * 340 * bagging_days * bagging_weeks * bagging_months)
		harvesting_cost = (harvesting_cost_per_bunch * bunch)
		packing_cost = packing_laborers * packing_cost_per_laborer * packing_days * packing_weeks * packing_months
		labor_cost = (spraying_cost + fertilizing_cost + weeding_cost + bagging_cost + harvesting_cost + packing_cost)
	
		total_cost = input_cost + materials_cost + labor_cost

		return input_cost, materials_cost, labor_cost, total_cost

st.header("Costs Incurred")
if st.button("Compute Production Costs"):
	if dataset == "Sto. Tomas, Davao del Norte - World Bank 2012":
		input_cost, materials_cost, lb_labor_cost, ub_labor_cost, lb_total_cost, ub_total_cost = calculate()
	
		st.markdown(f"<h3>INPUT COST PER HECTARE ANNUALLY: ₱{input_cost:.2f}</h3>", unsafe_allow_html=True)
		st.write(f"\n")
		st.markdown(f"<h3>MATERIALS COST PER HECTARE ANNUALLY: ₱{materials_cost:.2f}</h3>", unsafe_allow_html=True)
		st.write(f"\n")
		st.markdown(f"<h3>LABOR COST PER HECTARE ANNUALLY: ₱{lb_labor_cost:.2f} to ₱{ub_labor_cost:.2f}</h3>", unsafe_allow_html=True)
		st.write(f"\n")
		st.markdown(f"<h3>TOTAL COST PER HECTARE ANNUALLY: ₱{lb_total_cost:.2f} to ₱{ub_total_cost:.2f}</h3>", unsafe_allow_html=True)
		st.write(f"\n")

	elif dataset == "Sto. Tomas, Davao del Norte - CHED 2017":
		input_cost, materials_cost, labor_cost, total_cost = calculate()
		
		st.markdown(f"<h3>INPUT COST PER HECTARE ANNUALLY: ₱{input_cost:.2f}</h3>", unsafe_allow_html=True)
		st.write(f"\n")
		st.markdown(f"<h3>MATERIALS COST PER HECTARE ANNUALLY: ₱{materials_cost:.2f}</h3>", unsafe_allow_html=True)
		st.write(f"\n")
		st.markdown(f"<h3>LABOR COST PER HECTARE ANNUALLY: ₱{labor_cost:.2f}</h3>", unsafe_allow_html=True)
		st.write(f"\n")
		st.markdown(f"<h3>TOTAL COST PER HECTARE ANNUALLY: ₱{total_cost:.2f}</h3>", unsafe_allow_html=True)
		st.write(f"\n")
