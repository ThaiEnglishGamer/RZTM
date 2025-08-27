import os
import time
import sys

# --- Storing the ASCII Art directly as a multi-line string ---
# This is a more reliable way to ensure it always displays correctly.
TICKET_ART_STRING = r"""
................................................:xxxxxxxxxxxxk0KKKKKKKKKKKKKK00O0KKKKKKKKKKKKKKKKKKKKKKOkxxkxxkkxxxxxddddddddddxkO0XNWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNd'''''''''''''''''''''''''''''''''''''''''''''''''
................................................:xxxxxxxxxxxkKWWMMMMMMMMMMMMMMWWWMMMMMMMMMMMMMMMMMMMMMWN0xkxkxkkkkxxdddddddddddddooook0KXNWMMMMMMMWXNWMMMMMMMMMMMMMMMMMMMWNNWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWd'',,,,,,'''''''''''''''',,,,,,,,,'''''''cdc,oo;''
................................................:xxxxxxxxkkxkXMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWKkkkkxxddddddddddddddddo:,,,':ddxkO0KXNWWWOodKWMMMWNWMMMMMMMMMMMWNKKXNWMMMNOdcoKWXxodoo0KkkKWNKNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNKKNMWKKNMWXKNWNKKKNMMWd',;;;;;;,,,''''''''',,;::cccccllcc:;,'';kXOkKkc,,
.............';;,'.....'........................:xkkkkkkkkkxkXMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWKkkkxdllloddddddddddddddlc:cldxxkkkkkkOO0KxlldkKMMNKO0KXNWWMMMMMMWNNXXWMMMNOo.;X0;;loccOK00XKl;dNXKWXKNKOO0KKNXKXKO0KxoKMMXxdookoodlkkddlko:odXMMNd',,;;;;;;;,,''''''',:cccccccllllllllc:,cx000KOo:;
.............'dx;lc,:;:dl,',c:;lo...............:xkkkkkkkkkkkXMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWKkkkxolodddddddddxxdxdddddxxxxkkkkkkkkkkkkkxdddONWWWXOkkkOO0KXNWMMMMMMMMMMMWx.oNc.lxo,;0MMMWo:l;xdcKdclcxl:ccKxcxl:lkc:KMMWXklxo:OXclX0ooOddklxWMWd'',,,,,;;;,,'''''',:ccccllllllllllllllccldkkkolcc
..............co.lddd:lkOo:dkxcod...............:kkkkkkkkkkkOXMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWKkkxddddddddddddddooddxxxxkkkkkkkkkkkkkkkkkkkkkkOO0XNNKkxddddxkO0KXWWMMMMMMNc'ONc.dKx;cKMMM0ldOloxldoldldc:dldolOxllOkl0WMXd:oO0dodoOk:ck0kdxoOWMNd''''''',,,''''''',:ccccllllllllllllcccclxkxxdolcc
..............;,.''';;,,.;:';;..,...........:l..:kO00kkkkkkkOXMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMW0xxddddddddxdddxd;',,:dkkkkkkkkkkkkkkkkkkkkkkkkkkkkxxkOOxdddddddddxkOKXWWMMXdxNMXdoodkNMMMMNNWMWNWNXNNXkddkNNXNNWNXNWWXNMMWXXKXWWXXWWNXXXNWXXNMMMNx:,'''''''''''''.';ccccclllldxxollcccccccldxddlccc
..........lk;co:'.;:;:::;cdc;',:;,:;........o0,.:k0XKkkkkkkkk0NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNKkdddddddddddxxxxo,.:,.lkxxxdodkkkkkkkkkkkkkkkkkkxxddddxkxddxkddddddddddxkO0XNMMMMMMMMMMMMMMMMMMMMMMMMMMMMWWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNklc:;,''''''''...';ccccllldkkxollccccccccccccccccc
..........odckxxock0ooxldxxodkkkddxc........oK;.:k0XKkkkkkkkkkOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOkxddddddddddolc::;;:::,..,;;;;;;cxkkkkkkkkkkkkxdooooodddddxkxdxxddddddddddddddkOKXWMMMMMMMMMMMMWNNWMNNWWNNMMWNWMNWWNWMMMMMMWNNWMWNNWNNWMWNNWWWWNWMMMWkllll:,''''''.....':ccloxkkdlcllcccccccccccccccccc
..........,,.,;,;;;:'',',;;:;',:,,,.........dK:.:k0NKkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkxdddddddddddl;,,;;:cc:,'.'lxxxddxkkkkkc;dkkkxxoc,.....',,...',cddddddddddddddddddddxKWMMMMMWWWWMMKkk0NKkkOOOXWKdONOxOx0MMWXNMN0k0XOOOxOOKWOdOXOxOx0MMMNklllll:,'''.......'lxkOOxolccccccccccccccccccccclo
.  ......   .                .      ........dX:.:k0NKkkkkkkkkkkkxdooxkkkkkkkkkkkkkkkkkkkkkkkkkkkkxdddddo:cddddo,.,:cllc:;,,''okkx;;xOkkkl.:xxxddc'.              ..:odddddddddddddddxkKWMMMMMMMMWWMMXOOKNKOO000NN0O0K0OOOKWMWNWMNKOKXK00O00XWK0NN0OOOKWMMNklllll:''........,lxxdolcccccccccccccccccccccccokk
clllllllllllllllllllllllllllllllllllllllc'..dX:.:k0NKkkkkkkkkkkdllldkkkkkkkkkkkkkkkkkkkkkxdodxkkkxdlldddo;.:dddddoc::::::cldko.;kk:.lkkkko'.,;codc.                  .,c:::;:oddxxxkkkkKXOKN00NMMMMMMMMWWMMMWMMWMMMMMMMMMMMMMMMMMMMWWMMMWMMWMMMMMMMMMMMMMMMNklllc;'.........';;:cccccccccccccccccccccccloxkxoc
WMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMO;;kK:.:k0NX0OkkkkkkkkxxxkkkkkkkkOkkkOkkkkkko:'''''lxddc.;dddc.,odddxkkkxddxxkOOkx:.ckd',xxl:,'..;..cd;.                    .    .lkkkkkkkkONXkOXXNWMMMMMMMMMMMMMMMMMMMWNNWMWNWMMMMMMMMWNNWMMMMMMMMMMMMMMMMMWWMMNx::;,'.........'',,;:cccccccccccccccccccoxkOkxoc::
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMKxkKK:.:k0NNX0kkkkkkkkkkkkkkOkxolc:;::ldkOx;.,cdxl.'ldd;.cddd:..,,cxkd:;;;;;;;::;,,lkOx;',,,;cl:,,';ldc.  ..,;ldc'....           .:kkkkkkkkOXMOoKMMMWWWWMMMWNWWNWMMMMMXOxx0WKdk00OOOO0WKkkOOOO00OO0O00OO000Ok0MMNd''''.........''',,,;:ccccccccccccccccldxxdocc::::
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMKxkKK;.:k0NNX0kOOOOOOOOOOOkxl;'.',;:;,..ckkookOkxc.,odl.,oddl'..,.'dd,;oxkkkxdooodkkxddolcloooooooooodoc:okkkOKXX0xx0d.           ,xkkkkkO0KNWWWWMMMWWMMMMWOoddoxXMMMMNOkOXWK0OOK0OOOKWN0OOOO0KKkk0OK0OOOOOOOXWMWd'''....''.....'',,;:::cccccccccccccccllccccccc:::
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMKxk00;.ck0NNX0kOOOOOOOOOkd:'.,cdxkOOOkc..lOOOkkxl''cddl''co:.,ol:cdkxxkOOOOOOOkkxxddooooooooooodoodoodddokOccdOXNNNNNk'           .dOkkkkKWWWWMMMMMMWWWWMMW0dooodKWMMMMWWWMMMMMMMMMMMMMMMMMWKOKNNNXKKXXKKXXXNNXNWMWd'..'''''.......';::cc:cccccccccccccccccccccc:::::
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMKxx0O;.cO0NNN0OOOOOOOOOOo'.:dkOOOOOOOOd'.:kOkxdl,'cddddl;;;;lxOOOOOOOOOOOOOkkxxddoddooooooolloooooddddddoxO0KNNNNNNNNNk,....',;::coOOkkkkOXWWWMMMMMMMMWWWKkxdxOXX0OXWMMMMMMMMMMMMMMMMMMMMWOdkOOOOOkOkxkOkOkkdkNMWd'''';c:'......';:::cc:cccccccccccccccccccc:::::::
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM0dx0X0kKXNNNX0OOOOOOOOOOxoxOOkxdxxkOOOl..lkxddo;,cdddxxkOOkOOOOOOOOOOOOOkxdllloddddddddooolc:cooooddxxxkkkO0NWWNNNNNNNNKkkO00KKXXXXX0kkkxxxOXWMMMMMMMMWO:..  ..;oxxxdoc:::clokKWMMMMMMMMMMNXNNXXNNNNXXNNNWNKOKWMWd'',ck0Oxc.....;cc::::ccllllccccccccccccc:::::::::
xOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOx:;ONWWWWWWWWN0OOOOOOOOOOOOxdlc:::;:loc,.;oxdddl:lddxkOOOOOOOOOOdcxOOkkdc,......';,''',:ldoc::ldxxxkkOOOOOO00KKXNWWWMMMMWNXKXXXXXXXXX0xddddddx0NWMMMMWNd.         .,,.         .;dKWMMMMMMMMMMMMMMMMMMMMMMMMWXOxxkXNd',lO0Ok0d'...':::::::cclcclcccccccccccc::::::::::
......................................... '0WXOO0OOXWN0OOOOOOOOOOkolcldxxdoc:;,;codddddddxkOOOOOOOOOOOO0o,lkxdc..               .;ooodkOOOOOOOOOOOKXXXXNWMMMMMMNXOkxxdolclxkkxdddddddddxOXWMXk:.                          .dNMMMMMMMMMMMMMMMMMMMMMKl',,,xNd',lk0Oxd:.....';:::::ccccccccccccccccccc::::::c::
..........................................cXM0;;c;:0WNK00000000Oxllldk00000OkxdddddddxxkkO000OO00000OOOko':xd:.        .,.        'dOOOOOOOOOOOOO0XXXXKKKK0kdl:,.........,lddddddddddddddddl,.                             .lNMMMMMMMMMMMMMMMMMMMMNOk0KKNWd',,,;,'.........'',,,;:ccccccccccclolccc::::cdkxl
........................................'lKWW0;;c,:0WWNX0000000xllok0000000OkxdddddxkOO00000000000OOkkxxxo,;xl.     ..';xKd.        'xOOOOOOOOOOOOOOOkxdddc.   .. .cx;..,,,'':dddddddddddd:.                                 '0MMMMMMMMMMMMMMMMMMMMMMMMMMMWd,,''''................':cccccccloddoccc:::::cokxc
.....................................,lkXWWNW0;;c,;0WNWWNNXK000OxxO000000OkxdddddxkO0000000000OOkkxxxxxxd;,dd:;::::oOKXX0Kx'       .d0OOOOOkkkxxxddo:..'oko,.,cl:cdc. .'',,,coooodddddddo.                                  .oNMMMMMMMMMMMMMMMMMMMMMMMMMMNd,,,''''......'..........;ccloddddlccc:lxkl:::::;,
................................ .,lkXWWNNNNW0;,c,;0WNNNNWWWNXK00000000OkxxxxxxxxxxO0000000Oxoooooddxxxxx;'okOOo:;:xKXXOc;::,.     ,xOkxxxxdddodooooc.. .cOdcclllll;.,:ccllloooddoddddddd:.  ..''..      ....                .cKMMMMMMMMMMMMMMMMMMMMMMMMMNd,,,,,,''''.'dKo..........':loolccccoxoo0WOc;;,,'.
...............................'lkXNNNNNNNNXN0lldll0XXNNNNNNNWWNXKK000kxxxxkOO00Oxxk000OOkxxdc,,,,,;:oxkkl'd0K0xx0KX00XXKOookd,.  .cdddddddddddlc:;;,.....;::cllloooooooooodolodoodddddxxxoccdOKK0d,...,cdO0ko,.               cNMMMMMMMMMMMMMMMMMMMMMMMMWd,,,,,,,''''';c;.',,'....;c:'..'',,oKXXkdKXl''''..
.............................:kXNNNXXNNNNOloO00KKK00klo0NNNNXNNNNWNX0kxxkOO0KK0K00OOOkkxxxxxxdc,''''',cldl,oKKNNNNWWWWWNNNNNXX0d;;ldddddddddo:'.....',,;cloooooooooodddddddxl..:oxkkkkdodkkkOXNXNKdc;,:xXNXXXNKd;.             ;KMMMMMMMMMMWNXNMMMMMMMMMMWd,,,,,,,,,;lolcclk00kdoxOXNXd......cKKx;'dNO;'''''
...........................l0NNXXXXNNNNNO;.lO00KKK0Ok:.:0NNNNNXXXNNWN0O00KKKKKK0OOkxxxxxdolllllc:::;:;,'',.l0KXNNWMMMMMMWNNNNX0xdddddddddddl'  .,:loodddoodddddddxxxxxkkkkkkkl'..;cdkx:';dkk0XXNKc,xK0l,xNNNNNX0xlc:,'.....    :XMMMMMMMMWNXKKNWMMMMMMMMMWd,,,,,,,,;kNNXKXX0000KNWWNXXXc......,,...;0Nx;,,,,
.........................:ONNXXXXXXNNNWXx,'lkO0KKK0Ox:';kNNNNNNNXXXXNWWXKKKK0Okkxxxxxxkkdccccccccccccc:,''':xk0XNNWWWWWWNNNNNXkddxxxddddddd,  .:dxxxxxxxkkkkkkOOOOOOOOOOOOOkOOxl;. .,:;',lkOKXXXOlxXWWk'lXNXNOccolco0K0OO0k:. .oWMMMMMMMMWNXXNWMMMMMMMMMMWd,,,,,,,'c0NNXKXXK0KKKXXNNNNXOc..........'oNXl,,,,
........................oXWNXXXXXNNNNNWXx,'lkO0KKK0Ox:.;kNWNNNNNXXXXXNWWN0OkxxxxkkOOO00KOxddolccccccccc:;;ldOkkO0XWWWWWWWWWWN0kxxxxxxxxxkkx:. .'cdxkOOOOOOOOkkkxxxxxxxxxxkkkkOOOkd:.  .'cdkOKXX0Okkkxl:l0NNNXc;0MWx'xNXXNXNO' 'OWMWKdd0WMMMMMMMMMMMMMMMMMWd,,,,,,:oOXXNNNXXKKXXXXXXXXXXXKx;.........,kWO:,,'
'''',,,,;;;;:::ccccllllkNWNXXXXXNNNNNNWNx,.lkO0KKK0Ox:.;kNWNNNNNNNXXXXNWWKkkkOO00KKKKKKKKK00Oxolccccccccd0XNNXXKXWMMMMMMMMMMNOkOOOOOOOOO000x;.   ..',,,,;;:cllllllllllllllooddxxkkOd,. .:kkkOXNXXKKK0O0XXXNNNx;l0KdckXXXXKOc.,oOXMNkc..;o0WMMMMMMMMMMMMMMWd,,,,,lOKKKKKKKKKKKKXXKKKKKKKK0KOxoodo;....:KNd'''
00KKKXXXXXNNNWWWWWWMMMMWWNXKXXXNNNNNNNWNx'.lkO0KKK0Ox:.,kNWWNNNNNNXXXXXWWWXKKKKKKKK00OOOkkxxxxxxdoc:cc:l0NXNNNNXNWMMMMMMMMMMNK0000000OOkO0O0ko;..          .clllllllllc:;;:cllloodxkl.  'dOkk0XNXNKkxkkxdxxxxkOxxkkkO0KNN0dc;;,,:o0WWKx, .xWMMMMMMMMMMMMMWd,,;;cx0KKKKKXXXXKKKKK00KKKKKK00KXKKNNO;....oNK:.'
NNNNNNNNNWWWWWWWWWWWWWWWWNXNNNNWWWWWWWWWKxx0XXXNNNXXKOxkXWWWWWWWWWNNNNXNWWNK000OOkkxxxxxxxxxxxxkkkoc:::cdKXNNK0KXXNWMMMMMMMMX00000000OxlldO0OOOOxl;'........,cllllllllc'.  ...'',,,,,.   ;xkxkkOKXXdcxOkkxkkkOxoOXKKKKXNMMMMW0;    .xNMM0, ,0MMMMMMMMMMMMMWd,:clllx0KKXNX00KKKKK00000KKK000KXKKXkc'....,kWk,'
NNNNNNWWWWWWWWWWWWMMMMWWWWWWWWWWMMMMMMMWWWMWWMWMMMMMMMMMMMMMMMMMWWWWWWWWWWXkxxxxxxkkkkOOOOOO00000Kxc:::::lddo:;cdOKNMMMMMMMMWK000000kl:lxOOOOOOxolllcc::::cllllllllll:.               .,ldxOKXXXXN0xxkkxxkkkxxldXNNWMMMMMMMMWo.    'OWMNl .OMMMMMMMMMMMMMWd;clllld0KXNKxoloxKXXXKKK00000000KKXO:.......cKNo'
NWWWWWWWWWWWWMMMMMMMMWNNNNWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWNNNKOO00000KKKKKKKKKKKKKKKKxc::::::::;,,',:loooooooooooxkkkxxdlcodxxxdddlllllllllllllllllllllll;'.....   .....,codkKNNNXNNNNNWNNNNNNNKkkKNNNWMMMMMMMMMx.    .lNMKl,oXMMMMMMMMMMWWWWX0kolllxXXXXkllllo0XXXKOdoodO00000KKK0kc.....'dNO;
WWWWWWWWWMMMMMMMMMMMMWNNWWWWWNWWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWWNNWWWWNNXKKKK000kxkxxkOOOOOOkxdxl::::::::::;;;::,.        .,lc::;;;::lodddddlllllllllllllllllllllllllllcc:::::::cllooddOXNNNNNNNXOOOKNNNNNNNNNNNNNWMMMMMMMMk...,;ckWMMWNWMMMMMMMMMMMMMMWWXXKkdlllo0NXN0ollllkXXXKxlllloOXXXKxlodxo,....      
WWWWWWWWWWMMMMMMMMMMMWNXXNNNWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWNNXXXKOOkkkkxolllodxxxdoc;,,,;:::::::;'...'cdxxl;.. ..';,'''''''''';coddolllllllllllllllllllllllllllllloooooooooooddkKXNNNNNXklcclx0XNNNNNNXNNNWMMMWWNK0xlldOKkOWMMMMMMMMMMMMMMMMMMWWXXKkdlllo0NXN0ollllkXXXKxlllloOXXXKxlodxo,....      
NWWWWWWWWWWWWMMMMMMMMWNNNNNWWNWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWNWNNXXKKK000000OOkkOOOOdc::::;;::::::::,.   .lXWNNKd;',;:;;:c;,'''''''';ldollll:;;:cllllllllllllllllllllooooooooooooooloxO000kdlccccclkXXNNNNXNXKKK00OkxdddddxKWKOXMMMMMMMMMMMMMMMMMMMMMNx:llllxKNNXklllld0NXX0ollllxKKXXOollll:'...       
NWWWWWWMMMMMMMMMMMMMMWNXXXNNWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWKO00000000000000OO00xc::ccc::::::::::;'.   .lXKxl:;::;;;:ldd:''''''''',cllll;.,;..'clllllllllc;''':looooooooooooolcccccccccccccccccclkKXXNXX0xoodddddddddddkXMNkx0XWMMMMMMMMMMMMMMMMWd:llllkNNNKxllllxXNNXkllllo0XXX0dllll:'..         
::ccccllllooooddddxxxkXNNNNNWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWN0xxkkkkkkkkkkkkkxddoc:cloooollcc::::::;'.   .;c:;;;;;;;;;:okd;''''''''',:lll,.c0x:'.clllllll:.'do..looooooooooooocccccccccccccccccccccodxxxdllllodddddddddd0WMNkolo0WMMMMMMMMMMMMMMMWkclllo0NNXK0xolo0NXN0ollllkXNNXxllllc,.   .,,,:;. 
.....................'dKXXNNNWWWWWWWWWWWWWWWWWWWWWWWWWWWWWNNNXKK0OOxddddddddddddddddddoc:codoodddddolc::::::;'...';;;;;;;;;;;;oOOd;''''''''';cllc;.,:;..:llllllc..ld;.;ooooooooooooolccccccccccccccccccccclcccllllllloddddddddkXMMMWKdoONMMMMMMMMMMMMMMMWklllldKNNXK0kolxXNNXxlllldKNNNOollll;.. .;oOkcd0c.
.................... .cdxkO0XWWWWWWWWWWWWWWWWWWWNKK00OOOkkxxddoooooododddddddddddodooolclooooooooloool::::;;;;;;;;;;;;;;;;;;;;:dOOOxl,''''''',:llllc:;;:cllllllll:''',cooooooooooodkxl:cccccccccccccccccccclllllllllllloddddddd0WMMMMMNXWMMMWWWMMMMMMMMMMWkllllkXNNKxolloONNN0ollloONNNKdllll:,.';xocO0cc00x
                     .;cccclxXWWWWWWWWWWWWWWWWWWWK00kddddddddooooooooooooooooooooooooooolllllllllllllllcccc:;,;;;;;;;;;;;;;;;;:oxxxxxoc:;,,,,,;cllllllllllllllllloooooooooooooooookKKxlccccccccccccccccccccllllllllllllllodddxxONMMMMMMMMMMMWOxOKK0O00OXMMWkllllONNNOollldKNNXkllllxXNNXxllllc;;o0XXkokxo0Kox
                     .,:::::coxxxxxxxxxxxxxxxxxkkO0KOxddddddddddddddxdooooooooooooooooooooooooooooooooolcccc;.,c::::;;,,;;;;;;;:ccccccllcc:::cclllllllllllllllllooooooooooooooooolok0KkccccccccccccccccccllllllllllllllloxxxOKXWMMMMMMMMMMMNOxkkxdk0OkXMMWkllloKNNXxllllkNNN0olllo0NNNOooxkOO00XNXNNXKOOXXxx
                     .,;;:::::::::::::::;;::;:::okkOkxxxxxxxxxkkkkkkxxoooooooooooooolooooooooooooooooooollll:.'llcccc;,',,;;;;;;:cccccccccccccccllddololllllooooooooooooooooooollc:clolccccccccccccccccllllllllllllllllloxkkOXWMMWNNWMMMMWWNXNWWWWWWWWWMMWklllxXNNKdllldKWNXkllld0XXNX0OKXKO0NWWWWNNNXKKXNXX
                     .';;;;;;;;;;;;;;;;;;;;;;;;;lxkxxxxxxxxxxdolccldxxxxxxdoolloloolloooooooooooooooooooolloc.'lllllllc;,,,;;;;;;:cccccccccccccllokkololoddolooooooooooooooollcc:ccccccccccccccccccccclllllllllllllllllloxxkXWMNklll:lKNkccc:oKMMMMMMMMMMWklllkNNNXOollkNWW0olloOX0KNNNX0xoclx0NWMMMWWWNNNNX
                     ..,,,,,,,,,,,,,,,,,,''',,,,lxkkxdoodddddc,'ck0XNX0kO0xlxOl,',;:lllllllllllllllllllllllll..cllllllll:,';:;;;;:ccccccccccccclloxkxdodxOkolooooooolllllcccc:::ccccccccccccccccccccclllllllllllllllllllloxXWMMXddKO''ko.c00:.dWMMMWWWWWMWkllo0NXXNXxlo0WWXklllo0NXNNNKxlcc:::cxXNNWWMMMMWWN
                      .',''''''''',,,,,'....''''cdxxdlccoddddddkXWMWNNX0ddOOdc.    .,clccccccccccccccccccllll'.:lllllllc;',:c:;;;:cccccccccccccclloxxkkkxdoooolllcccc::::::::::cccccccccccccccccccccllllllllllllllllllllcdKWMMMMW0o;cOO''0MX:.xWMW0ooooOWWklldKNNNNNOoxXWN0ollldXNNNNXkccc::::ckNNXkdxkOKXNN
                       .''''''''''''''''.......':dddolccoddddddxO000Oxdl::;,.      ...,ccllllllllllllllccclcc,.;lllllll:,';clc:;:clllllcclllllllcllloooooooollccccccc:cccccccccccccccccccccclllclllllllllllllllllllllllokXMMMMNOc.'lkX0,.okc'oOdxXNKKKKNMWkllkNWNKOOdo0NWNklllo0WWNNNKo::::::::okxoc;;;;;:cc
                        ........................:ooolc::lodooooddodl'.     ...........,ccodoooooooooooolcloloc,:oolloolc;,coolccclooooolclooooolcloodddddoollllllolllccloolllllllllllooooollooocoddoodddoddodoodollllld0WMMMMMXdlloloKW0olld0W0oxNMMMMMMMWkllONWXxclcdXWW0olllxXWNXXNKkxxdoc:cccccccc::;;;,,
                         .......................;ooolc::looooooooooc'.......'''..''''',ccclcccccllcclcccccccc;.'cccccc;,,,:cc::::clclllccccclcccccccccccccccccccccc:::::ccccccccccccccccccccccclllccllllllllllllllllllllldKWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWklo0WWKolllkNWNklllo0NWNKXNXWWWWNKkdlccllcclcc;,,,
"""

# --- FIXED VARIABLES ---
TICKET_PRICE = 20
TOTAL_TICKETS = 10000

# --- DYNAMIC VARIABLES ---
tickets_left = TOTAL_TICKETS

# --- MINIMUM TERMINAL SIZE ---
MIN_WIDTH = 100
MIN_HEIGHT = 25
# The width required by the ASCII art is large, so we adjust our minimum.
ART_MIN_WIDTH = 170 

def clear_screen():
    """Clears the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def get_terminal_size():
    """Gets the current size of the terminal."""
    try:
        columns, rows = os.get_terminal_size()
        return columns, rows
    except OSError:
        return 80, 24 # Default size if detection fails

def get_ticket_art_lines():
    """Returns the pre-made ASCII art as a list of lines."""
    return TICKET_ART_STRING.split('\n')

def draw_header(width):
    """Draws the main program header."""
    title = "(R)ecreation (Z)one (T)icket (M)anager"
    print("─" * width)
    print(f"{title:^{width}}")
    print("─" * width)

def draw_main_layout(content_func):
    """
    The main drawing function that handles screen size and layout.
    It takes another function as an argument to render the main content.
    """
    clear_screen()
    width, height = get_terminal_size()

    if width < MIN_WIDTH or height < MIN_HEIGHT:
        print("TERMINAL TOO SMALL".center(width))
        return

    draw_header(width)

    sidebar_width = 25
    main_content_width = width - sidebar_width - 3
    
    tickets_sold = TOTAL_TICKETS - tickets_left
    
    sidebar_lines = [
        "┌───────────────────────┐",
        "│      TICKET INFO      │",
        "├───────────────────────┤",
        f"│ Price: {TICKET_PRICE} THB".ljust(sidebar_width-1) + "│",
        f"│ Tickets Left: {tickets_left}".ljust(sidebar_width-1) + "│",
        f"│ Tickets Sold: {tickets_sold}".ljust(sidebar_width-1) + "│",
        "└───────────────────────┘",
        "",
        "┌───────────────────────┐",
        "│        CONTROLS       │",
        "├───────────────────────┤",
        "│ [B] Buy Tickets       │",
        "│ [M] Main Menu (Art)   │",
        "│ [H] Help              │",
        "│ [Q] Quit              │",
        "└───────────────────────┘",
    ]

    main_content_lines = content_func(main_content_width, height - 5)

    max_lines = max(len(sidebar_lines), len(main_content_lines))
    for i in range(max_lines):
        side_line = sidebar_lines[i] if i < len(sidebar_lines) else " " * sidebar_width
        main_line = main_content_lines[i] if i < len(main_content_lines) else ""
        print(f"{side_line} │ {main_line}")

    print("─" * width)

def content_home(width, height):
    """Content for the home screen, shows the ticket art."""
    term_width, _ = get_terminal_size()
    if term_width < ART_MIN_WIDTH:
        return [
            "",
            "Terminal is too narrow to display ticket art.",
            f"Please expand the window to at least {ART_MIN_WIDTH} columns.",
        ]
    
    art_lines = get_ticket_art_lines()
    # No vertical centering, as the art is quite large
    return art_lines

def content_help(width, height):
    """Content for the help menu."""
    return [
        "",
        "RZTM HELP MANUAL",
        "────────────────",
        "",
        "This program is designed to manage ticket sales for the school's",
        "Recreation Zone anniversary event.",
        "",
        "  [B] - Enter the BUYING MENU",
        "        This is where you process ticket sales.",
        "",
        "  [M] - Return to the MAIN MENU",
        "        This screen displays the ASCII art of the event ticket.",
        "",
        "  [H] - Display this HELP screen",
        "",
        "  [Q] - QUIT the program",
    ]
    
def buy_tickets_flow():
    """Handles the entire ticket purchasing process."""
    global tickets_left
    width, _ = get_terminal_size()

    if tickets_left == 0:
        message_line = "SOLD OUT!".center(width)
        print(message_line, end="\r")
        time.sleep(2)
        return

    while True:
        try:
            prompt = "→ How many tickets to purchase? (Enter a number): "
            print(prompt, end="")
            num_to_buy_str = input()
            if not num_to_buy_str: continue

            num_to_buy = int(num_to_buy_str)
            if num_to_buy <= 0:
                print("! Please enter a positive number.")
            elif num_to_buy > tickets_left:
                print(f"! Not enough tickets left. Only {tickets_left} available.")
            else:
                break
        except ValueError:
            print("! Invalid input. Please enter a number.")
            
    total_price = num_to_buy * TICKET_PRICE
    print(f"→ Total Price: {total_price} THB")
    
    while True:
        try:
            prompt = f"→ Money Received (must be at least {total_price} THB): "
            print(prompt, end="")
            money_received_str = input()
            if not money_received_str: continue

            money_received = float(money_received_str)
            if money_received < total_price:
                print(f"! Insufficient payment. Received {money_received}, but need {total_price}.")
            else:
                break
        except ValueError:
            print("! Invalid input. Please enter a valid amount.")

    change = money_received - total_price
    tickets_left -= num_to_buy
    
    print(f"✓ Purchase complete! Change to give back: {change:.2f} THB")
    print("Press [Enter] to continue...")
    input()

def main():
    """Main program loop."""
    current_screen_func = content_home
    
    while True:
        draw_main_layout(current_screen_func)
        
        width, _ = get_terminal_size()
        if width < MIN_WIDTH:
            print("Please resize window to continue. Press [Q] to quit: ", end="")
        else:
            print("Enter command [B, M, H, Q]: ", end="")
        
        sys.stdout.flush()
        choice = input().lower()

        if choice == 'q':
            break
        elif choice == 'b':
            buy_tickets_flow()
        elif choice == 'm':
            current_screen_func = content_home
        elif choice == 'h':
            current_screen_func = content_help

    clear_screen()
    print("\nThank you for using RZTM!\n")

if __name__ == "__main__":
    main()