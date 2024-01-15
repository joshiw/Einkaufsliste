import random
import cowsay
Komplimente = ["Du bist ein Top G", "Du bist eine Frühlingsrolle", "Wow, du hast 4 Milionen Power in Rise of Kingdom", "Du bist ein Macher", "Hier sitzt ein Ehrenmann"]

my_karateka = r'''
 ,.
 \-'__
/ o.__o____ 
\/_/ /.___/--,
  ||\'
  | /
  \_\
  -'' mrf
'''
my_chessboard = r'''
                  _        _        _        __       __       _
        /\       |_)      /        | \      |_       |_       /        |_|
       /--\      |_)      \_       |_/      |__      |        \_?      | |

  _           #########         #########         #########         #########
 (_)   [`'`'] ##\`.'/##  ':v:`  ##/\:/\##  |:+:|  ##':v:`##  \`.'/  ##[`'`']#
 (_)    |::|  ##(o:o)##  (o:0)  #/(o:o)\#  (o:o)  ##(o:0)##  (o:o)  ###|::|##
        |::|  ###\:/:\#   (:)   ###(:)###   (:)   ###(:)###   \:/:\ ###|::|##
              ####"####         #########         #########    "    #########
  __ #########    _    #########    _    #########    _    #########    _
   / ###(:)###   (:)   ###(:)###   (:)   ###(:)###   (:)   ###(:)###   (:)
  /  ###|:|###   |:|   ###|:|###   |:|   ###|:|###   |:|   ###|:|###   |:|
     ###|:|###   |:|   ###|:|###   |:|   ###|:|###   |:|   ###|:|###   |:|
     #########         #########         #########         #########
              #########         #########         #########         #########
  /           #########         #########         #########         #########
 (_)          #########         #########         #########         #########
              #########         #########         #########         #########
              #########         #########         #########         #########
  _  #########         #########         #########         #########
 |_  #########         #########         #########         #########
  _) #########         #########         #########         #########
     #########         #########         #########         #########
     #########         #########         #########         #########
   .          #########         #########         #########         #########
  /|          #########         #########         #########         #########
 '-|          #########         #########         #########         #########
              #########         #########         #########         #########
              #########         #########         #########         #########
  _  #########         #########         #########         #########
  _) #########         #########         #########         #########
  _) #########         #########         #########         #########
     #########         #########         #########         #########
     #########         #########         #########         #########
  _      _    #########    _    #########    _    #########    _    #########
   )    (_)   ###(_)###   (_)   ###(_)###   (_)   ###(_)###   (_)   ###(_)###
  /_    | |   ###| |###   | |   ###| |###   | |   ###| |###   | |   ###| |###
        |_|   ###|_|###   |_|   ###|_|###   |_|   ###|_|###   |_|   ###|_|###
              #########         #########         #########         #########
     #########         #########   ___   #########         #########
  /| ##[`'`']#  \`~'/  ##'\v/`##  /\*/\  ##|`+'|##  '\v/`  ##\`~'/##  [`'`']
   | ###|  |##  (o o)  ##(o 0)## /(o o)\ ##(o o)##  (o 0)  ##(o o)##   |  |
     ###|__|##   \ / \ ###(_)###   (_)   ###(_)###   (_)   ###\ / \#   |__|
     #########    "    #########         #########         ####"####
'''
my_boxer = r'''
     .,,cddHHHHHHHHDDp,.
                                                                        .,dHHHHHHHHHHHHHHHHHHDp,..
                                                                    .,dHHHHHHHHHHHHHHHHHHHHHHHHHHDp,.
                                                                .,cdHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHD,.
                                                              .dHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHDp,.
                                                             dHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHD,
                                                            dHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHD,
                                                           dHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHD,.
                                                           HHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHD,
                                                           cHHHHHHHHHHHHHHHHHHHHHD"'     '"dHHHHHHHHHHHHHHH GGGGD
                                                            "CHHHHHHHHHHHHHHHHD"'             ''""dhhhhhhhh     G
                                                              "CHHHHHHHDP""''                       '"(hhhh ()  G
                                                               W"                                     "hhhh    GD
                                                               W                                              GD.
                                                               W                                          "GGG"WD
                                                               W                  HHHHHHHHHH                    W
                                                              dWHHHHHHHH        HH  JjghjJ  H                  .W
                                                              h  JJjghJ H          8  ##  8                   .WW
                                                              W 8    ##8 .:        *JjghjJ*                  .W.WD
                                                              W *JjghjJ* :                                 .WWD "WD
                                                              cW         :                                .WD    "WD
                                                              cW        :    ...                        .WWD      WWWD
                                                              W         :    .."                       .wD      g. "WWWD
                                                              W.         """"                        .WWD       dg   "WWWWWWWD
                                                              dW.                                   .WD          g.         "WWWWWWWWWD
                                                               dW.                                .WWD           dg.                 "WWWWWWWD
                                                                dW.    .cKKKKKKKKKD.             .WD              dg.                       "WWWWWD
                                                                 dW.   KK : : : : KK           .WwD                dg                            "WWWWD
                                                                  dW.  "CKKKKKKKKKD"          .WD                   g.                               "WWWD
                                                                   dW.                      .WWD                    dg                                  "WWD
                                                                    dW.                  .WWWD"WW.                   g.                                   "WWWWD
                                                                     dWw.             .WWWD  .WDdWWW.                dg     dW                                "WWWD
                                                                       dWW.         .WWWD .WWWD     W.                g   dW"                                    "WWD
                                                                         dWW.     .WWD .WWWD       dwg.               w dW"                                        "WWD
                                                                           dWWWWWWWD .WWD        dww "g         g     w.W"                                           "WD
                                                                                    .WD        dww"             dgg   dW"                                             "WD
                                                                                    WD       dww"                 dgg.W"                                               "WD
                                                                                   .W       dw"                      W"                                       W         "W
                                                                                   WD      dw"                      dW                                       dW          W
                                                                                   W      dw"                       W"                                       W"          W
                                                                                   WD     w"                        W                                        W           WD
                                                                                   "WD   dw                         W                                        W.          "W
                                                                                    "W   w"                         W                                        dW           W
                                                                                     WD dw                          W.                                        W           W
                                                                                     "W w"                          dW.                                       W           W
                                                                                     dW w                            dW                                       W.          WD
                                                                                    dW" w                             W.                                      dW          "W
                                                                                    W" dw                             dW                                       W           W
                                                                                   dW  w"                              W.                                      W           W
                                                                                  dW"  w                  dW          dWW.                                     W           W
                                                                                  W"   w.                dW"          W"dWW.                                   W.          W
                                                                                 dW    dw.               W"          dW   dWW.                                 dW          WD
                                                                                 W"     dw.              W           W"     dw.                                 W          "W
                                                                                dW       dw             dW          dW       dw.                                W.          W
                                                                                W"        w.            W"         dW"        dhh                               dW          W
                                                                                d         dw.           W          W"           dh                               W          W
                                                                                W          dw.          W.        dW                                             W          W
                                                                                W           dw.         dW.       W"                                             W          W
                  dGGGGGGGGGGGGGGD                                              W            dwe         dW.     dW                                              W          W
             dGGGGG"'          '"GGGGGGD                                        W.            Wde         dW.    W"                                              W.         W
        dGGGGG"'                     '"GGGGD                                    dW.           W"de         dW   dW                                               dW         W
      dGG"'                              '"GGGGGD    dGGGGGD                    dW.          dW                 W"                                                W         W
    dGG"'                                     '"GGGGGG"'":GWWWWWWWD              dW.         W"                 W                                                 W         WD
  dGG"'                                           ::    .G      '"WWWWWWWD        dW.        W                 dW                                                 W         "W
 dG"'                                            .::    G              '"WWWWWWWWD dW.       W                 W"                                                 W          W
 G"                                              ::'    G                      '"WWWWW.      W                 W                                                 dW          W
dG                                               ::    .G                           '"W      W                 W                                                 W"          W
GG                                               ::    G"                                    W                 W.                                                W           W
GG                                               ::    G                                    dW                 dW                                                W          .W
GG                                           dGGGGGGGGDG                                    W"                  W.                                              dW          WD
GG                                     dGGGGGG"'    '"GGGGGGGD                              W                   dWW.                                           dW"          W
GG                                dGGGGG"'                 '"GGGD                           W                     dW.                                          W"           W
GG                            dGGGG"'                         '"GGGGD      dGGGGGGp         W                      dW.                                        dW            W
dG                         dGGG"'                                 '"GGGGGGGG"'  '"d         W                       dW.           dWWWW                      dW"           .W
"g                      dGGG"'                                         "::"       GWWWWWWWWWWWWWWWWWWD               dW. dWWWWWWWWW"                         W"            WD
 G.       gggg.        dG"'                                             ::        G                 "WWWWWWWWWWWWWWWWWWWWW"                                 dW             W
 dG.         "ggggg.  dG"                                               ::.       G                                                                         W"             W
  dG.             "gggG"                                                '::      .G                                                                        dW             .W
   dGG.              dG                                                  ::      dG                                                                        W"             WD
     dGG.            GG                                                  ::      GD                                                                       dW              W
       dGG.          GG                                                  ::      G"                                                                       W"             .W
         dGGGGG.     GG                                                  ::      G                                                                        W              WD
              dGGGGGGGG                                                 .::      G                                                                       dW              W
                    dGG                                                 ::'      G                                                                       W"              W
                     GG.                                                ::       G                                                                       W               W
                     dGG                                                ::       G                                                                      dW               W
                      GG                                                ::       G                                                                      W"               W
                      GG                                                ::       G    wwwwwwD                                                          dW               .W
                      dG                                               .::,.     G.         wwwwwwwD                                                   W"               WD
                       G.                                           .,GG::GG,. .,GWWWWWD           wwD                                                dW                W
                       dG,                                       .,GGGD.::. GGGGGP     WWWWWWWWWWWWWWWWD                                             dW"                W
                        dG,.                                 .,GGGGD  .:' :               WD          dWWWWWWWWWWWWWD                               dW"                dW
                         dGG,.                         ,.GGGGGGD      :'  :              KKKKKKKKKKKKKKKKKKKKKKKKKKKWWWWWWWWWWWWWWWWWWWWD          dWKKKKKKKKKKKKKKKKKKKK
                           dgg,.       GGGGGGD,.,dGGGGGGGD            ;   ;              kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkWWWWWWWWWWWWkkkkkkkkkkkkkkkkkkkkkD
                             dgg,.          dGGGGGD.,gD                                 dkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk
                               dggg,.            .,ggD                                  wD                                                                            dW
                                  dgggg,.     .,gggD                                    w                                                                              WD
                                      dgggggggggD              WILU                    wD                                                                               K
                                      '''
cowsay.draw(random.choice(Komplimente),my_boxer)
cowsay.draw(random.choice(Komplimente),my_chessboard)
cowsay.draw(random.choice(Komplimente),my_karateka)