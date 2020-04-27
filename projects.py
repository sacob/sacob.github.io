import plotly.figure_factory as ff

df = [dict(Task="ESF-ALL4HER", Start='2019-01', Finish='2021-03', Lead = 'Fatih'),
      dict(Task="ISFP-EDUC8", Start='2020-01', Finish='2021-12', Lead = 'Onur'),
      dict(Task="SPECKHARD", Start='2020-01', Finish='2021-12', Lead = 'Onur'),
      dict(Task="AMIF-ORIENT8", Start='2021-01', Finish='2022-12', Lead = 'Samet'),
      dict(Task="AMIF-EMMIWO", Start='2021-01', Finish='2022-12',Lead = 'Sevgi'),
      dict(Task="H2020-NOMADIC", Start='2020-09', Finish='2023-02',Lead = 'Sevgi'),
      dict(Task="REC-ARTEMIS", Start='2021-01', Finish='2022-12',Lead = 'Samet'),
      dict(Task="H2020-ACTESET", Start='2021-05', Finish='2023-11', Lead = 'Aziz'),
      dict(Task="H2020-PREPOL4EU", Start='2021-05', Finish='2023-11', Lead = 'Saban'),
      dict(Task="H2020-SU-AI03-Goffi", Start='2021-05', Finish='2023-11', Lead = 'None'),
      dict(Task="H2020-SU-FCT01", Start='2021-05', Finish='2023-11', Lead = 'Onur'),
      dict(Task="ESF-Transnational", Start='2020-09', Finish='2022-12', Lead = 'Fatih'),
      dict(Task="H2020-SU- DS02-Embry-Riddle", Start='2021-05', Finish='2023-11', Lead = 'None'),
      dict(Task="H2020-SU- FCT03-Embry-Riddle", Start='2021-05', Finish='2023-11', Lead = 'None'),
      dict(Task="AI Summit with VUB", Start='2020-02', Finish='2020-09', Lead = 'Saban'),
      dict(Task="CW Transformation", Start='2020-01', Finish='2020-08', Lead = 'Samet')]

fig = ff.create_gantt(df, show_colorbar=True, showgrid_x=True, showgrid_y=True, title='Projects Timeline', height=800, index_col='Lead')
fig.show()
fig.write_html("Gantt2.html")
