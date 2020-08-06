#make plot1
UUEE_shere_Rus = data["UUEE"]
EDDF_Fran_Ger = data["EDDF"]
RJBB_Kan_Jap = data["RJBB"]
YSSY_Syd_Aust = data["YSSY"]
KATL_Atl_USA = data["KATL"]
CYYZ_Tor_Can = data["CYYZ"]
fig, (ax1, ax2, ax3, ax4, ax5, ax6) = plt.subplots(6,1,figsize=(20,20))
fig.suptitle('departures number for 6 airports during March and April')
ax1.set_title('UUEE')
ax2.set_title('EDDF')
ax3.set_title('RJBB')
ax4.set_title('YSSY')
ax5.set_title('KATL')
ax6.set_title('CYYZ')
ax1.set_ylabel('Departures per day')
ax2.set_ylabel('Departures per day')
ax3.set_ylabel('Departures per day')
ax4.set_ylabel('Departures per day')
ax5.set_ylabel('Departures per day')
ax6.set_ylabel('Departures per day')
ax3.set_xlabel('date')
ax1.plot(data.index, UUEE_shere_Rus)
ax2.plot(data.index, EDDF_Fran_Ger)
ax3.plot(data.index, RJBB_Kan_Jap)
ax4.plot(data.index, YSSY_Syd_Aust)
ax5.plot(data.index, KATL_Atl_USA)
ax6.plot(data.index, CYYZ_Tor_Can)
plt.legend()
plt.savefig('plot1.png')
