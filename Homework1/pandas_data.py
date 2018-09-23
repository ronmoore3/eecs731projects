import pandas as pd

df1 = pd.read_excel('C:\\Users\\Ronald\\Documents\\college-majors\\recent-grads.xlsx', 0, usecols=[3], na_values=['NA']).iloc[:30]
df2 = pd.read_excel('C:\\Users\\Ronald\\Documents\\college-majors\\recent-grads.xlsx', 0, usecols=[4], na_values=['NA']).iloc[:30]
df3 = pd.read_excel('C:\\Users\\Ronald\\Documents\\college-majors\\recent-grads.xlsx', 0, usecols=[5], na_values=['NA']).iloc[:30]
df4 = pd.read_excel('C:\\Users\\Ronald\\Documents\\college-majors\\recent-grads.xlsx', 0, usecols=[14], na_values=['NA']).iloc[:30]


ax1 = df1.plot.bar(x=None, y=None, rot=0)
ax1.set_ylim(0,130000)
ax1.set_xlabel("Major")
ax1.set_ylabel("Number of Graduates")

ax2 = df2.plot.bar(x=None, y=None, rot=0)
ax2.set_xlabel("Major")
ax2.set_ylabel("Number of Graduates")

ax3 = df3.plot.bar(x=None, y=None, rot=0)
ax3.set_xlabel("Major")
ax3.set_ylabel("Number of Graduates")

ax4 = df4.plot.bar(x=None, y=None, rot=0)
ax4.set_xlabel("Major")
ax4.set_ylabel("Unemployment Rate")

fig1 = ax1.get_figure()
fig1.savefig("total.pdf")

fig2 = ax2.get_figure()
fig2.savefig("men.pdf")

fig3 = ax3.get_figure()
fig3.savefig("women.pdf")

fig4 = ax4.get_figure()
fig4.savefig("unemployment.pdf")