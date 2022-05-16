from django import forms
from django.shortcuts import render
from .models import Get
import tokenization_program.utils.helper as helper
from tokenization_program.tokenize.token_search import search_token

# Create your views here.
def token_search(request):
    return render(request, 'tokens_app/token_search.html', {})

def search_results(request):
    tokens = request.GET['token']
    tokens = helper.get_token_list(tokens)
    search_result = search_token(tokens)
    tokens_url = helper.get_urls(search_result['found'])
    search_result['found'] = tokens_url
    return render(request, 'tokens_app/search_results.html', {'results': search_result})

def resources_2(request):
        return render(request, "002.html",{})


def resources_3(request):
        return render(request, "003.html",{})


def resources_4(request):
        return render(request, "004.html",{})


def resources_5(request):
        return render(request, "005.html",{})


def resources_6(request):
        return render(request, "006.html",{})


def resources_7(request):
        return render(request, "007.html",{})


def resources_8(request):
        return render(request, "008.html",{})


def resources_9(request):
        return render(request, "009.html",{})


def resources_10(request):
        return render(request, "010.html",{})


def resources_11(request):
        return render(request, "011.html",{})


def resources_12(request):
        return render(request, "012.html",{})


def resources_13(request):
        return render(request, "013.html",{})


def resources_14(request):
        return render(request, "014.html",{})


def resources_15(request):
        return render(request, "015.html",{})


def resources_16(request):
        return render(request, "016.html",{})


def resources_17(request):
        return render(request, "017.html",{})


def resources_18(request):
        return render(request, "018.html",{})


def resources_19(request):
        return render(request, "019.html",{})


def resources_20(request):
        return render(request, "020.html",{})


def resources_21(request):
        return render(request, "021.html",{})


def resources_22(request):
        return render(request, "022.html",{})


def resources_23(request):
        return render(request, "023.html",{})


def resources_24(request):
        return render(request, "024.html",{})


def resources_25(request):
        return render(request, "025.html",{})


def resources_26(request):
        return render(request, "026.html",{})


def resources_27(request):
        return render(request, "027.html",{})


def resources_28(request):
        return render(request, "028.html",{})


def resources_29(request):
        return render(request, "029.html",{})


def resources_30(request):
        return render(request, "030.html",{})


def resources_31(request):
        return render(request, "031.html",{})


def resources_32(request):
        return render(request, "032.html",{})


def resources_33(request):
        return render(request, "033.html",{})


def resources_34(request):
        return render(request, "034.html",{})


def resources_35(request):
        return render(request, "035.html",{})


def resources_36(request):
        return render(request, "036.html",{})


def resources_37(request):
        return render(request, "037.html",{})


def resources_38(request):
        return render(request, "038.html",{})


def resources_39(request):
        return render(request, "039.html",{})


def resources_40(request):
        return render(request, "040.html",{})


def resources_41(request):
        return render(request, "041.html",{})


def resources_42(request):
        return render(request, "042.html",{})


def resources_43(request):
        return render(request, "043.html",{})


def resources_44(request):
        return render(request, "044.html",{})


def resources_45(request):
        return render(request, "045.html",{})


def resources_46(request):
        return render(request, "046.html",{})


def resources_47(request):
        return render(request, "047.html",{})


def resources_48(request):
        return render(request, "048.html",{})


def resources_49(request):
        return render(request, "049.html",{})


def resources_50(request):
        return render(request, "050.html",{})


def resources_51(request):
        return render(request, "051.html",{})


def resources_52(request):
        return render(request, "052.html",{})


def resources_53(request):
        return render(request, "053.html",{})


def resources_54(request):
        return render(request, "054.html",{})


def resources_55(request):
        return render(request, "055.html",{})


def resources_56(request):
        return render(request, "056.html",{})


def resources_57(request):
        return render(request, "057.html",{})


def resources_58(request):
        return render(request, "058.html",{})


def resources_59(request):
        return render(request, "059.html",{})


def resources_60(request):
        return render(request, "060.html",{})


def resources_61(request):
        return render(request, "061.html",{})


def resources_62(request):
        return render(request, "062.html",{})


def resources_63(request):
        return render(request, "063.html",{})


def resources_64(request):
        return render(request, "064.html",{})


def resources_65(request):
        return render(request, "065.html",{})


def resources_66(request):
        return render(request, "066.html",{})


def resources_67(request):
        return render(request, "067.html",{})


def resources_68(request):
        return render(request, "068.html",{})


def resources_69(request):
        return render(request, "069.html",{})


def resources_70(request):
        return render(request, "070.html",{})


def resources_71(request):
        return render(request, "071.html",{})


def resources_72(request):
        return render(request, "072.html",{})


def resources_73(request):
        return render(request, "073.html",{})


def resources_74(request):
        return render(request, "074.html",{})


def resources_75(request):
        return render(request, "075.html",{})


def resources_76(request):
        return render(request, "076.html",{})


def resources_77(request):
        return render(request, "077.html",{})


def resources_78(request):
        return render(request, "078.html",{})


def resources_79(request):
        return render(request, "079.html",{})


def resources_80(request):
        return render(request, "080.html",{})


def resources_81(request):
        return render(request, "081.html",{})


def resources_82(request):
        return render(request, "082.html",{})


def resources_83(request):
        return render(request, "083.html",{})


def resources_84(request):
        return render(request, "084.html",{})


def resources_85(request):
        return render(request, "085.html",{})


def resources_86(request):
        return render(request, "086.html",{})


def resources_87(request):
        return render(request, "087.html",{})


def resources_88(request):
        return render(request, "088.html",{})


def resources_89(request):
        return render(request, "089.html",{})


def resources_90(request):
        return render(request, "090.html",{})


def resources_91(request):
        return render(request, "091.html",{})


def resources_92(request):
        return render(request, "092.html",{})


def resources_93(request):
        return render(request, "093.html",{})


def resources_94(request):
        return render(request, "094.html",{})


def resources_95(request):
        return render(request, "095.html",{})


def resources_96(request):
        return render(request, "096.html",{})


def resources_97(request):
        return render(request, "097.html",{})


def resources_98(request):
        return render(request, "098.html",{})


def resources_99(request):
        return render(request, "099.html",{})


def resources_100(request):
        return render(request, "100.html",{})


def resources_101(request):
        return render(request, "101.html",{})


def resources_102(request):
        return render(request, "102.html",{})


def resources_103(request):
        return render(request, "103.html",{})


def resources_104(request):
        return render(request, "104.html",{})


def resources_105(request):
        return render(request, "105.html",{})


def resources_106(request):
        return render(request, "106.html",{})


def resources_107(request):
        return render(request, "107.html",{})


def resources_108(request):
        return render(request, "108.html",{})


def resources_109(request):
        return render(request, "109.html",{})


def resources_110(request):
        return render(request, "110.html",{})


def resources_111(request):
        return render(request, "111.html",{})


def resources_112(request):
        return render(request, "112.html",{})


def resources_113(request):
        return render(request, "113.html",{})


def resources_114(request):
        return render(request, "114.html",{})


def resources_115(request):
        return render(request, "115.html",{})


def resources_116(request):
        return render(request, "116.html",{})


def resources_117(request):
        return render(request, "117.html",{})


def resources_118(request):
        return render(request, "118.html",{})


def resources_119(request):
        return render(request, "119.html",{})


def resources_120(request):
        return render(request, "120.html",{})


def resources_121(request):
        return render(request, "121.html",{})


def resources_122(request):
        return render(request, "122.html",{})


def resources_123(request):
        return render(request, "123.html",{})


def resources_124(request):
        return render(request, "124.html",{})


def resources_125(request):
        return render(request, "125.html",{})


def resources_126(request):
        return render(request, "126.html",{})


def resources_127(request):
        return render(request, "127.html",{})


def resources_128(request):
        return render(request, "128.html",{})


def resources_129(request):
        return render(request, "129.html",{})


def resources_130(request):
        return render(request, "130.html",{})


def resources_131(request):
        return render(request, "131.html",{})


def resources_132(request):
        return render(request, "132.html",{})


def resources_133(request):
        return render(request, "133.html",{})


def resources_134(request):
        return render(request, "134.html",{})


def resources_135(request):
        return render(request, "135.html",{})


def resources_136(request):
        return render(request, "136.html",{})


def resources_137(request):
        return render(request, "137.html",{})


def resources_138(request):
        return render(request, "138.html",{})


def resources_139(request):
        return render(request, "139.html",{})


def resources_140(request):
        return render(request, "140.html",{})


def resources_141(request):
        return render(request, "141.html",{})


def resources_142(request):
        return render(request, "142.html",{})


def resources_143(request):
        return render(request, "143.html",{})


def resources_144(request):
        return render(request, "144.html",{})


def resources_145(request):
        return render(request, "145.html",{})


def resources_146(request):
        return render(request, "146.html",{})


def resources_147(request):
        return render(request, "147.html",{})


def resources_148(request):
        return render(request, "148.html",{})


def resources_149(request):
        return render(request, "149.html",{})


def resources_150(request):
        return render(request, "150.html",{})


def resources_151(request):
        return render(request, "151.html",{})


def resources_152(request):
        return render(request, "152.html",{})


def resources_153(request):
        return render(request, "153.html",{})


def resources_154(request):
        return render(request, "154.html",{})


def resources_155(request):
        return render(request, "155.html",{})


def resources_156(request):
        return render(request, "156.html",{})


def resources_157(request):
        return render(request, "157.html",{})


def resources_158(request):
        return render(request, "158.html",{})


def resources_159(request):
        return render(request, "159.html",{})


def resources_160(request):
        return render(request, "160.html",{})


def resources_161(request):
        return render(request, "161.html",{})


def resources_162(request):
        return render(request, "162.html",{})


def resources_163(request):
        return render(request, "163.html",{})


def resources_164(request):
        return render(request, "164.html",{})


def resources_165(request):
        return render(request, "165.html",{})


def resources_166(request):
        return render(request, "166.html",{})


def resources_167(request):
        return render(request, "167.html",{})


def resources_168(request):
        return render(request, "168.html",{})


def resources_169(request):
        return render(request, "169.html",{})


def resources_170(request):
        return render(request, "170.html",{})


def resources_171(request):
        return render(request, "171.html",{})


def resources_172(request):
        return render(request, "172.html",{})


def resources_173(request):
        return render(request, "173.html",{})


def resources_174(request):
        return render(request, "174.html",{})


def resources_175(request):
        return render(request, "175.html",{})


def resources_176(request):
        return render(request, "176.html",{})


def resources_177(request):
        return render(request, "177.html",{})


def resources_178(request):
        return render(request, "178.html",{})


def resources_179(request):
        return render(request, "179.html",{})


def resources_180(request):
        return render(request, "180.html",{})


def resources_181(request):
        return render(request, "181.html",{})


def resources_182(request):
        return render(request, "182.html",{})


def resources_183(request):
        return render(request, "183.html",{})


def resources_184(request):
        return render(request, "184.html",{})


def resources_185(request):
        return render(request, "185.html",{})


def resources_186(request):
        return render(request, "186.html",{})


def resources_187(request):
        return render(request, "187.html",{})


def resources_188(request):
        return render(request, "188.html",{})


def resources_189(request):
        return render(request, "189.html",{})


def resources_190(request):
        return render(request, "190.html",{})


def resources_191(request):
        return render(request, "191.html",{})


def resources_192(request):
        return render(request, "192.html",{})


def resources_193(request):
        return render(request, "193.html",{})


def resources_194(request):
        return render(request, "194.html",{})


def resources_195(request):
        return render(request, "195.html",{})


def resources_196(request):
        return render(request, "196.html",{})


def resources_197(request):
        return render(request, "197.html",{})


def resources_198(request):
        return render(request, "198.html",{})


def resources_199(request):
        return render(request, "199.html",{})


def resources_200(request):
        return render(request, "200.html",{})


def resources_201(request):
        return render(request, "201.html",{})


def resources_202(request):
        return render(request, "202.html",{})


def resources_203(request):
        return render(request, "203.html",{})


def resources_204(request):
        return render(request, "204.html",{})


def resources_205(request):
        return render(request, "205.html",{})


def resources_206(request):
        return render(request, "206.html",{})


def resources_207(request):
        return render(request, "207.html",{})


def resources_208(request):
        return render(request, "208.html",{})


def resources_209(request):
        return render(request, "209.html",{})


def resources_210(request):
        return render(request, "210.html",{})


def resources_211(request):
        return render(request, "211.html",{})


def resources_212(request):
        return render(request, "212.html",{})


def resources_213(request):
        return render(request, "213.html",{})


def resources_214(request):
        return render(request, "214.html",{})


def resources_215(request):
        return render(request, "215.html",{})


def resources_216(request):
        return render(request, "216.html",{})


def resources_217(request):
        return render(request, "217.html",{})


def resources_218(request):
        return render(request, "218.html",{})


def resources_219(request):
        return render(request, "219.html",{})


def resources_220(request):
        return render(request, "220.html",{})


def resources_221(request):
        return render(request, "221.html",{})


def resources_222(request):
        return render(request, "222.html",{})


def resources_223(request):
        return render(request, "223.html",{})


def resources_224(request):
        return render(request, "224.html",{})


def resources_225(request):
        return render(request, "225.html",{})


def resources_226(request):
        return render(request, "226.html",{})


def resources_227(request):
        return render(request, "227.html",{})


def resources_228(request):
        return render(request, "228.html",{})


def resources_229(request):
        return render(request, "229.html",{})


def resources_230(request):
        return render(request, "230.html",{})


def resources_231(request):
        return render(request, "231.html",{})


def resources_232(request):
        return render(request, "232.html",{})


def resources_233(request):
        return render(request, "233.html",{})


def resources_234(request):
        return render(request, "234.html",{})


def resources_235(request):
        return render(request, "235.html",{})


def resources_236(request):
        return render(request, "236.html",{})


def resources_237(request):
        return render(request, "237.html",{})


def resources_238(request):
        return render(request, "238.html",{})


def resources_239(request):
        return render(request, "239.html",{})


def resources_240(request):
        return render(request, "240.html",{})


def resources_241(request):
        return render(request, "241.html",{})


def resources_242(request):
        return render(request, "242.html",{})


def resources_243(request):
        return render(request, "243.html",{})


def resources_244(request):
        return render(request, "244.html",{})


def resources_245(request):
        return render(request, "245.html",{})


def resources_246(request):
        return render(request, "246.html",{})


def resources_247(request):
        return render(request, "247.html",{})


def resources_248(request):
        return render(request, "248.html",{})


def resources_249(request):
        return render(request, "249.html",{})


def resources_250(request):
        return render(request, "250.html",{})


def resources_251(request):
        return render(request, "251.html",{})


def resources_252(request):
        return render(request, "252.html",{})


def resources_253(request):
        return render(request, "253.html",{})


def resources_254(request):
        return render(request, "254.html",{})


def resources_255(request):
        return render(request, "255.html",{})


def resources_256(request):
        return render(request, "256.html",{})


def resources_257(request):
        return render(request, "257.html",{})


def resources_258(request):
        return render(request, "258.html",{})


def resources_259(request):
        return render(request, "259.html",{})


def resources_260(request):
        return render(request, "260.html",{})


def resources_261(request):
        return render(request, "261.html",{})


def resources_262(request):
        return render(request, "262.html",{})


def resources_263(request):
        return render(request, "263.html",{})


def resources_264(request):
        return render(request, "264.html",{})


def resources_265(request):
        return render(request, "265.html",{})


def resources_266(request):
        return render(request, "266.html",{})


def resources_267(request):
        return render(request, "267.html",{})


def resources_268(request):
        return render(request, "268.html",{})


def resources_269(request):
        return render(request, "269.html",{})


def resources_270(request):
        return render(request, "270.html",{})


def resources_271(request):
        return render(request, "271.html",{})


def resources_272(request):
        return render(request, "272.html",{})


def resources_273(request):
        return render(request, "273.html",{})


def resources_274(request):
        return render(request, "274.html",{})


def resources_275(request):
        return render(request, "275.html",{})


def resources_276(request):
        return render(request, "276.html",{})


def resources_277(request):
        return render(request, "277.html",{})


def resources_278(request):
        return render(request, "278.html",{})


def resources_279(request):
        return render(request, "279.html",{})


def resources_280(request):
        return render(request, "280.html",{})


def resources_281(request):
        return render(request, "281.html",{})


def resources_282(request):
        return render(request, "282.html",{})


def resources_283(request):
        return render(request, "283.html",{})


def resources_284(request):
        return render(request, "284.html",{})


def resources_285(request):
        return render(request, "285.html",{})


def resources_286(request):
        return render(request, "286.html",{})


def resources_287(request):
        return render(request, "287.html",{})


def resources_288(request):
        return render(request, "288.html",{})


def resources_289(request):
        return render(request, "289.html",{})


def resources_290(request):
        return render(request, "290.html",{})


def resources_291(request):
        return render(request, "291.html",{})


def resources_292(request):
        return render(request, "292.html",{})


def resources_293(request):
        return render(request, "293.html",{})


def resources_294(request):
        return render(request, "294.html",{})


def resources_295(request):
        return render(request, "295.html",{})


def resources_296(request):
        return render(request, "296.html",{})


def resources_297(request):
        return render(request, "297.html",{})


def resources_298(request):
        return render(request, "298.html",{})


def resources_299(request):
        return render(request, "299.html",{})


def resources_300(request):
        return render(request, "300.html",{})


def resources_301(request):
        return render(request, "301.html",{})


def resources_302(request):
        return render(request, "302.html",{})


def resources_303(request):
        return render(request, "303.html",{})


def resources_304(request):
        return render(request, "304.html",{})


def resources_305(request):
        return render(request, "305.html",{})


def resources_306(request):
        return render(request, "306.html",{})


def resources_307(request):
        return render(request, "307.html",{})


def resources_308(request):
        return render(request, "308.html",{})


def resources_309(request):
        return render(request, "309.html",{})


def resources_310(request):
        return render(request, "310.html",{})


def resources_311(request):
        return render(request, "311.html",{})


def resources_312(request):
        return render(request, "312.html",{})


def resources_313(request):
        return render(request, "313.html",{})


def resources_314(request):
        return render(request, "314.html",{})


def resources_315(request):
        return render(request, "315.html",{})


def resources_316(request):
        return render(request, "316.html",{})


def resources_317(request):
        return render(request, "317.html",{})


def resources_318(request):
        return render(request, "318.html",{})


def resources_319(request):
        return render(request, "319.html",{})


def resources_320(request):
        return render(request, "320.html",{})


def resources_321(request):
        return render(request, "321.html",{})


def resources_322(request):
        return render(request, "322.html",{})


def resources_323(request):
        return render(request, "323.html",{})


def resources_324(request):
        return render(request, "324.html",{})


def resources_325(request):
        return render(request, "325.html",{})


def resources_326(request):
        return render(request, "326.html",{})


def resources_327(request):
        return render(request, "327.html",{})


def resources_328(request):
        return render(request, "328.html",{})


def resources_329(request):
        return render(request, "329.html",{})


def resources_330(request):
        return render(request, "330.html",{})


def resources_331(request):
        return render(request, "331.html",{})


def resources_332(request):
        return render(request, "332.html",{})


def resources_333(request):
        return render(request, "333.html",{})


def resources_334(request):
        return render(request, "334.html",{})


def resources_335(request):
        return render(request, "335.html",{})


def resources_336(request):
        return render(request, "336.html",{})


def resources_337(request):
        return render(request, "337.html",{})


def resources_338(request):
        return render(request, "338.html",{})


def resources_339(request):
        return render(request, "339.html",{})


def resources_340(request):
        return render(request, "340.html",{})


def resources_341(request):
        return render(request, "341.html",{})


def resources_342(request):
        return render(request, "342.html",{})


def resources_343(request):
        return render(request, "343.html",{})


def resources_344(request):
        return render(request, "344.html",{})


def resources_345(request):
        return render(request, "345.html",{})


def resources_346(request):
        return render(request, "346.html",{})


def resources_347(request):
        return render(request, "347.html",{})


def resources_348(request):
        return render(request, "348.html",{})


def resources_349(request):
        return render(request, "349.html",{})


def resources_350(request):
        return render(request, "350.html",{})


def resources_351(request):
        return render(request, "351.html",{})


def resources_352(request):
        return render(request, "352.html",{})


def resources_353(request):
        return render(request, "353.html",{})


def resources_354(request):
        return render(request, "354.html",{})


def resources_355(request):
        return render(request, "355.html",{})


def resources_356(request):
        return render(request, "356.html",{})


def resources_357(request):
        return render(request, "357.html",{})


def resources_358(request):
        return render(request, "358.html",{})


def resources_359(request):
        return render(request, "359.html",{})


def resources_360(request):
        return render(request, "360.html",{})


def resources_361(request):
        return render(request, "361.html",{})


def resources_362(request):
        return render(request, "362.html",{})


def resources_363(request):
        return render(request, "363.html",{})


def resources_364(request):
        return render(request, "364.html",{})


def resources_365(request):
        return render(request, "365.html",{})


def resources_366(request):
        return render(request, "366.html",{})


def resources_367(request):
        return render(request, "367.html",{})


def resources_368(request):
        return render(request, "368.html",{})


def resources_369(request):
        return render(request, "369.html",{})


def resources_370(request):
        return render(request, "370.html",{})


def resources_371(request):
        return render(request, "371.html",{})


def resources_372(request):
        return render(request, "372.html",{})


def resources_373(request):
        return render(request, "373.html",{})


def resources_374(request):
        return render(request, "374.html",{})


def resources_375(request):
        return render(request, "375.html",{})


def resources_376(request):
        return render(request, "376.html",{})


def resources_377(request):
        return render(request, "377.html",{})


def resources_378(request):
        return render(request, "378.html",{})


def resources_379(request):
        return render(request, "379.html",{})


def resources_380(request):
        return render(request, "380.html",{})


def resources_381(request):
        return render(request, "381.html",{})


def resources_382(request):
        return render(request, "382.html",{})


def resources_383(request):
        return render(request, "383.html",{})


def resources_384(request):
        return render(request, "384.html",{})


def resources_385(request):
        return render(request, "385.html",{})


def resources_386(request):
        return render(request, "386.html",{})


def resources_387(request):
        return render(request, "387.html",{})


def resources_388(request):
        return render(request, "388.html",{})


def resources_389(request):
        return render(request, "389.html",{})


def resources_390(request):
        return render(request, "390.html",{})


def resources_391(request):
        return render(request, "391.html",{})


def resources_392(request):
        return render(request, "392.html",{})


def resources_393(request):
        return render(request, "393.html",{})


def resources_394(request):
        return render(request, "394.html",{})


def resources_395(request):
        return render(request, "395.html",{})


def resources_396(request):
        return render(request, "396.html",{})


def resources_397(request):
        return render(request, "397.html",{})


def resources_398(request):
        return render(request, "398.html",{})


def resources_399(request):
        return render(request, "399.html",{})


def resources_400(request):
        return render(request, "400.html",{})


def resources_401(request):
        return render(request, "401.html",{})


def resources_402(request):
        return render(request, "402.html",{})


def resources_403(request):
        return render(request, "403.html",{})


def resources_404(request):
        return render(request, "404.html",{})


def resources_405(request):
        return render(request, "405.html",{})


def resources_406(request):
        return render(request, "406.html",{})


def resources_407(request):
        return render(request, "407.html",{})


def resources_408(request):
        return render(request, "408.html",{})


def resources_409(request):
        return render(request, "409.html",{})


def resources_410(request):
        return render(request, "410.html",{})


def resources_411(request):
        return render(request, "411.html",{})


def resources_412(request):
        return render(request, "412.html",{})


def resources_413(request):
        return render(request, "413.html",{})


def resources_414(request):
        return render(request, "414.html",{})


def resources_415(request):
        return render(request, "415.html",{})


def resources_416(request):
        return render(request, "416.html",{})


def resources_417(request):
        return render(request, "417.html",{})


def resources_418(request):
        return render(request, "418.html",{})


def resources_419(request):
        return render(request, "419.html",{})


def resources_420(request):
        return render(request, "420.html",{})


def resources_421(request):
        return render(request, "421.html",{})


def resources_422(request):
        return render(request, "422.html",{})


def resources_423(request):
        return render(request, "423.html",{})


def resources_424(request):
        return render(request, "424.html",{})


def resources_425(request):
        return render(request, "425.html",{})


def resources_426(request):
        return render(request, "426.html",{})


def resources_427(request):
        return render(request, "427.html",{})


def resources_428(request):
        return render(request, "428.html",{})


def resources_429(request):
        return render(request, "429.html",{})


def resources_430(request):
        return render(request, "430.html",{})


def resources_431(request):
        return render(request, "431.html",{})


def resources_432(request):
        return render(request, "432.html",{})


def resources_433(request):
        return render(request, "433.html",{})


def resources_434(request):
        return render(request, "434.html",{})


def resources_435(request):
        return render(request, "435.html",{})


def resources_436(request):
        return render(request, "436.html",{})


def resources_437(request):
        return render(request, "437.html",{})


def resources_438(request):
        return render(request, "438.html",{})


def resources_439(request):
        return render(request, "439.html",{})


def resources_440(request):
        return render(request, "440.html",{})


def resources_441(request):
        return render(request, "441.html",{})


def resources_442(request):
        return render(request, "442.html",{})


def resources_443(request):
        return render(request, "443.html",{})


def resources_444(request):
        return render(request, "444.html",{})


def resources_445(request):
        return render(request, "445.html",{})


def resources_446(request):
        return render(request, "446.html",{})


def resources_447(request):
        return render(request, "447.html",{})


def resources_448(request):
        return render(request, "448.html",{})


def resources_449(request):
        return render(request, "449.html",{})


def resources_450(request):
        return render(request, "450.html",{})


def resources_451(request):
        return render(request, "451.html",{})


def resources_452(request):
        return render(request, "452.html",{})


def resources_453(request):
        return render(request, "453.html",{})


def resources_454(request):
        return render(request, "454.html",{})


def resources_455(request):
        return render(request, "455.html",{})


def resources_456(request):
        return render(request, "456.html",{})


def resources_457(request):
        return render(request, "457.html",{})


def resources_458(request):
        return render(request, "458.html",{})


def resources_459(request):
        return render(request, "459.html",{})


def resources_460(request):
        return render(request, "460.html",{})


def resources_461(request):
        return render(request, "461.html",{})


def resources_462(request):
        return render(request, "462.html",{})


def resources_463(request):
        return render(request, "463.html",{})


def resources_464(request):
        return render(request, "464.html",{})


def resources_465(request):
        return render(request, "465.html",{})


def resources_466(request):
        return render(request, "466.html",{})


def resources_467(request):
        return render(request, "467.html",{})


def resources_468(request):
        return render(request, "468.html",{})


def resources_469(request):
        return render(request, "469.html",{})


def resources_470(request):
        return render(request, "470.html",{})


def resources_471(request):
        return render(request, "471.html",{})


def resources_472(request):
        return render(request, "472.html",{})


def resources_473(request):
        return render(request, "473.html",{})


def resources_474(request):
        return render(request, "474.html",{})


def resources_475(request):
        return render(request, "475.html",{})


def resources_476(request):
        return render(request, "476.html",{})


def resources_477(request):
        return render(request, "477.html",{})


def resources_478(request):
        return render(request, "478.html",{})


def resources_479(request):
        return render(request, "479.html",{})


def resources_480(request):
        return render(request, "480.html",{})


def resources_481(request):
        return render(request, "481.html",{})


def resources_482(request):
        return render(request, "482.html",{})


def resources_483(request):
        return render(request, "483.html",{})


def resources_484(request):
        return render(request, "484.html",{})


def resources_485(request):
        return render(request, "485.html",{})


def resources_486(request):
        return render(request, "486.html",{})


def resources_487(request):
        return render(request, "487.html",{})


def resources_488(request):
        return render(request, "488.html",{})


def resources_489(request):
        return render(request, "489.html",{})


def resources_490(request):
        return render(request, "490.html",{})


def resources_491(request):
        return render(request, "491.html",{})


def resources_492(request):
        return render(request, "492.html",{})


def resources_493(request):
        return render(request, "493.html",{})


def resources_494(request):
        return render(request, "494.html",{})


def resources_495(request):
        return render(request, "495.html",{})


def resources_496(request):
        return render(request, "496.html",{})


def resources_497(request):
        return render(request, "497.html",{})


def resources_498(request):
        return render(request, "498.html",{})


def resources_499(request):
        return render(request, "499.html",{})


def resources_500(request):
        return render(request, "500.html",{})


def resources_501(request):
        return render(request, "501.html",{})


def resources_502(request):
        return render(request, "502.html",{})


def resources_503(request):
        return render(request, "503.html",{})


def resources_simple(request):
    return render(request, 'simple.html', {})

def resources_medium(request):
    return render(request, 'medium.html', {})

def resources_hard(request):
    return render(request, 'hard.html', {})
