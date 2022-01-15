import plotly_express as px
from src.data.data import RegsFoods
from src.data.data_constants import CALS, DAY_NAME, FOOD_NAME, DATE, WEEK, AGGREAGABLE_FIELDS
from src.data.data_utils import tail

def fig_all_days(regs_food_merge):
    return px.bar(tail(RegsFoods.to_visualizable(regs_food_merge), DATE, 5), x=DATE, y=CALS, color=FOOD_NAME, hover_data=AGGREAGABLE_FIELDS, text=DAY_NAME)\
        .update_layout(xaxis_type='category').update_xaxes(categoryorder='category ascending')

def fig_all_weeks(regs_food_merge):
    return px.bar(tail(RegsFoods.to_visualizable(regs_food_merge), WEEK, 5), x=WEEK, y=CALS, color=FOOD_NAME, hover_data=AGGREAGABLE_FIELDS)
