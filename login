<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
        <title>Đăng nhập :: Quản lý đào tạo - TRƯỜNG CAO ĐẲNG NGHỀ KIÊN GIANG</title>
        <meta http-equiv="X-UA-Compatible" content="IE=EmulateIE10"/>
        <meta name="robots" content="index, follow" />
        <meta name="keywords" content="" />
        <meta name="description" content="CUSC" />
        <meta name="generator" content="CUSC - Can Tho University Softwave Center" />
        <meta http-equiv="cache-control" content="public" />
        
        <link rel="stylesheet" type="text/css" href="http://daotao.caodangnghekg.edu.vn/templates/kgvc/css/template.css"/>
        <link rel="stylesheet" type="text/css" href="http://daotao.caodangnghekg.edu.vn/templates/kgvc/excite-bike/jquery-ui-1.8.11.custom.css"/>
        <link rel="stylesheet" type="text/css" href="http://daotao.caodangnghekg.edu.vn/templates/kgvc/excite-bike/datepicker.css"/>
        <link rel="icon" type="image/png" href="http://daotao.caodangnghekg.edu.vn/templates/kgvc/favicon.png" />
        <script type="text/javascript">
    var textCmbc = '---- Vui lòng chọn ----';
    var textCmba = '---- Tất cả ----';
    var textSubmitNotSel = 'Vui lòng chọn dòng cần xử lý';
    var textConfirmDel = 'Thực hiện xóa các dòng được chọn?';    
    var textNotSearch = 'Không thể lọc thông tin do dữ liệu đã bị khóa.';    
    //
    var textPleSel = 'Vui lòng chọn';
    var textAll = 'Tất cả';
    var textDeDel = 'Bỏ chọn';
    var textSel = 'Chọn';
    var textConfLogout = 'Xác nhận thoát khỏi chương trình?';
    var textErrInitialSem = 'Dữ liệu năm học - học kỳ chưa được khởi tạo.';
    var miniumChar = 'Số ký tự tối thiểu là';
    var quangan = 'Quá ngắn';
    var trungbinh = 'Trung bình';
    var weak = 'Yếu';
    var veryweak = 'Rất yếu';
    var strong = 'Mạnh';
    var verystrong = 'Rất mạnh';
    var notsafe = 'Mật khẩu không an toàn!';
    
    var textSTT = 'Stt';
    var textThanhPhan = 'Thành phần';
    var textSapXep = 'Sắp xếp';
    var textDelete = 'Xóa';
    
    var textExists = 'Thành phần đã có trên danh sách';
    
    var hdLanguageSession = 'vn';
    
    var enterPassword = 'Vui lòng nhập mật khẩu';
    
    var minimumChar = 'Số ký tự tối thiểu của mật khẩu là 8';
    var minimumChar5 = 'Số ký tự tối thiểu của mật khẩu là 5';
    
    var notMatchPass = 'Mật khẩu và Mật khẩu nhắc lại không khớp nhau';
    
    var changePassSuccess = 'Đổi mật khẩu thành công.';
        
    var reLoginpass = 'Có lỗi xảy ra! Vui lòng đăng nhập lại để thực hiện chức năng đổi mật khẩu.';
    
    var notfound = 'Không tìm thấy thông tin';
    
    var session_en = null;
        var requreChangePass = '';
    var format_sep = '-';
</script>        <script type="text/javascript" language="javascript" src="http://daotao.caodangnghekg.edu.vn/script/jquery-1.6.2.min.js"></script>
        <script type="text/javascript" language="javascript" src="http://daotao.caodangnghekg.edu.vn/script/jquery.ui.core.js"></script>
        <script type="text/javascript" language="javascript" src="http://daotao.caodangnghekg.edu.vn/script/jquery.ui.widget.js"></script>
        <script type="text/javascript" language="javascript" src="http://daotao.caodangnghekg.edu.vn/script/jquery.ui.mouse.js"></script>
        <script type="text/javascript" language="javascript" src="http://daotao.caodangnghekg.edu.vn/script/jquery-ui-1.8.14.custom.min.js"></script>
        <script type="text/javascript" language="javascript" src="http://daotao.caodangnghekg.edu.vn/script/jquery.ui.datepicker.js"></script>
        <script type="text/javascript" language="javascript" src="http://daotao.caodangnghekg.edu.vn/script/jquery-ui-timepicker-addon.js"></script>
        <script type="text/javascript" language="javascript" src="http://daotao.caodangnghekg.edu.vn/script/jquery.ui.draggable.js"></script>
        <script type="text/javascript" language="javascript" src="http://daotao.caodangnghekg.edu.vn/script/jquery.cookie.js"></script>
        <script type="text/javascript" language="javascript" src="http://daotao.caodangnghekg.edu.vn/script/jquery.fixedtableheader.min.js"></script>
        <script type="text/javascript" language="javascript" src="http://daotao.caodangnghekg.edu.vn/script/jquery.pstrength-min.1.2.js"></script>
        <script type="text/javascript" language="javascript" src="http://daotao.caodangnghekg.edu.vn/script/global.js"></script>
        <script type="text/javascript" language="javascript" src="http://daotao.caodangnghekg.edu.vn/script/jquery.multiselect.min.js"></script>
        <script type="text/javascript" language="javascript" src="http://daotao.caodangnghekg.edu.vn/script/fillter/jquery.multiselect.filter.js"></script>
        <link rel="stylesheet" type="text/css" href="http://daotao.caodangnghekg.edu.vn/script/fillter/jquery.multiselect.filter.css"/>
        <!--[if lte IE 7]>
            <script type='text/javascript'>
                alert('Hiện tại Website chúng tôi không hỗ trợ trình duyệt Internet Explore phiên bản cũ vì nó đã quá lỗi thời và không ổn định, hãy sử dụng Firefox hoặc Chrome để có thể sử dụng đầy đủ các chức năng của Website chúng tôi, xin cảm ơn!');
                location = "http://daotao.caodangnghekg.edu.vn/download.html";
            </script>
        <![endif]-->
    </head>
    <body id="body">
                <table class="mainbody" width="100%" border="0" cellpadding="0" cellspacing="0" align="center">
            <tr>
                <td valign="top" style="padding: 0px; height: 300px;">
                    <div name='dlg_frmLookup' id='dlg_frmLookup' style='width:750px; margin-left:-375px; z-index:9999' class='fixed modal gradient_modal'>
                <table width='100%'>
                    <tr>
                        <td class='left'><div class='bold white text-shadow lower_case' name='sp_frmLookup_Title' id='sp_frmLookup_Title'>Tìm kiếm thông tin</div></td>
                        <td class='right' width='20%'><span class='pointer bold white dlg_close right' onclick='hideModal("dlg_frmLookup");' title='Nhấn ESC hoặc nhấn [x] để đóng'>[X]</span></td>
                    </tr>
                </table><div id='div_frmLookup_content'>
                <table id='tb_msg_frmLookup' style='background-color:#FFFFFF;display:none' width='100%' border='0' cellpadding='0' cellspacing='0' align='center'>
                    <tr><td><div class='error' sub='ul_frmLookup'>Thông báo lỗi<span>Ẩn/Hiện</span></div></td></tr>
                    <tr><td><ul id='ul_frmLookup' class='error'></ul></td></tr>
                </table>
                <table id='tb_msg_frmLookup_success' style='background-color:#FFFFFF;display:none' width='100%' border='0' cellpadding='0' cellspacing='0' align='center'>
                    <tr><td><div class='success' sub='ul_frmLookup'>Thông báo<span>Ẩn/Hiện</span></div></td></tr>
                    <tr><td><ul id='ul_frmLookup_success' class='success'></ul></td></tr>
                </table><form name='frm_frmLookup' id='frm_frmLookup' method='post' autocomplete='off' >
                <input type="hidden" name="h_frmLookup_id" id="h_frmLookup_id" value ="" /><div style="position:relative;max-height:520px;height: expression(this.scrollHeight > 520 ? 'px' : 'auto' );overflow-x:none;overflow-y:auto "><table id='tb_frmLookup' name='tb_frmLookup' width='100%' class="soft fixheader" >
<tr >
<td  align='left' width='35%' colspan='4' ><div id="tb_additional"></div></td>
</tr>
<tr >
<td  align='right' width='35%' ><label name='lb_lookup_title' id='lb_lookup_title' ></label></td>
<td  ><input type='textbox' name='txt_lookup_value' id='txt_lookup_value' value = '' maxlength='250' tabname="lookup"  />&nbsp;<input type='button' name='btnSearch' id='btnSearch' value='Tìm' onclick="getLookup();" tabsubmit="lookup"  /></td>
</tr>
<tr >
<td  align='left' width='35%' colspan='2' ><fieldset  id = 'fr_lookup'><legend>Danh sách kết quả</legend><div id="div_lookup"></div></fieldset></td>
</tr>
</table></div><table id='tb_tbs_frmLookup' name='tb_tbs_frmLookup' width='100%' class="soft fixheader" >
<tr >
<td  align='center' colspan = '2' align = 'center' tabsubmit='frmLookup'><div id='div_footer_lookup' ></div></td>
</tr>
<tr style="display:none" id="tr_frmLookup_ext_notes" >
<td  ><span id='sp_frmLookup_ext_notes'></span></td>
</tr>
</table></form></div></div>
 <link rel="stylesheet" type="text/css" href="http://daotao.caodangnghekg.edu.vn/templates/kgvc/css/template_login.css"/>
<div id="header">
    <div id="banner">
        <div id="div-control">
        </div>
    </div>
</div>
<form action="http://daotao.caodangnghekg.edu.vn/login/login" id="frmMain" name="frmMain" method="post" autocomplete="on">
    <div id="page-body"> 
        <table id="table-main" style="min-width: 780;width: 80%;" align="center" border="0" cellpadding="0" cellspacing="0">
            <tr>
                <td width="400" align="center" valign="top" style="vertical-align:top;">
                    <form method="post" action="detect.php" name="frmLogin" autocomplete="off">
                        <table id="login-sv" class="login" width="100%" align="center" border="0" cellpadding="0" cellspacing="0">
                            <tr>
                                <td class="bg-module-top"></td>
                            </tr>
                            <tr>
                                <td align="center" class="bg-module-middle">
                                    <input type="text" id="txt_Login_ten_dang_nhap" class="username-login" name="txt_Login_ten_dang_nhap" id="txt_Login_ten_dang_nhap" value="" placeholder="Mã số đăng nhập"/>
                                    <input type="password" id="pw_Login_mat_khau" class="password-login" name="pw_Login_mat_khau" id="pw_Login_mat_khau" value="" placeholder="Mật khẩu" />
                                </td>
                            </tr>
                            
                            <tr>
                                <td align="center" class="bg-module-middle">
                                    <div style="padding-top: 13px;float: left;padding-left:27px;font-size: 13px;">
									<a href="/doimatkhau" target="blank" style="color: #06548E;font-weight: bold;">Quên mật khẩu</a>
									</div>
                                    <div style="padding-left: 210px;"><input type="submit" class="btn-login-form" name="bt_Login_submit" value="" /></div>
                                </td>
                            </tr>
                            <tr>
                                <td class="bg-module-bottom" colspan="2">&nbsp;</td>
                            </tr>
                        </table>
                    </form>

                </td>
                <td width="40" align="center" valign="top">&nbsp;</td>
                <td id="module-thongbao" align="left" valign="top">
                 
                </td>
            </tr>
        </table>
    </div>
</form>
<div id="footer">
        <p class="top">Số 1022 Nguyễn Trung Trực, P. An Hòa, TP. Rạch Giá, Kiên Giang</p>
        <p>Điện thoại: 02973.814.946 (P. Tổ chức hành chính) - 02973.814.947 (Tư vấn Học nghề)</p>
    </td>
</div><script>
    
    
$(document).ready(function() {
    window.addEventListener("load", function(event) {
        var url = "http://daotao.caodangnghekg.edu.vn/capcha/securimage_show.php?sid="+Math.random();
        setTimeout(function(){
            $("#verify_code").attr('src',url);
        },100);
    });
    
    $("input[name='bt_Login_submit']").click(function(){
        
        var date = new Date();
        date.setTime(date.getTime() + (5 * 24 * 60 * 60 * 1000));
        var options = {
            path: '/',
            expires: date
        };    

        $.cookie("login_cookie", 'none', options);
        
    });
    
    
    
});    
    
    
    
function hienThiThongBao(dlg_id, url, id) {
    $('#overlay').slideDown();
    $('#'+dlg_id).show('puff');
    var data = "id=" + id;
    /***/
    showLoading();
    $.ajax({
        type: "GET",
        url: url + "&cache=" + Math.random(),
        dataType: 'json',
        data: data,
        async: false,
        success: function(result){
            var title = result.title;
            var nguoitao = result.nguoitao;
            var content = result.content;
            if(content !== "") {            
                $("#poptitle").html(title);
                $("#popnguoitao").html($('<div/>').html(nguoitao).text());
                $("#popcontent").html($('<div/>').html(content).text());
                $('#loading').hide();
            } else {
                $("#poptitle").html("Không thể hiển thị thông báo lúc này! Vui lòng liên hệ Quản trị hệ thống!");
                $("#popnguoitao").html("");
                $("#popcontent").html("");
                $('#loading').hide();
            }
        }
    });
}
</script> 
                </td>
            </tr>
        </table>
                <div id="overlay">&nbsp;</div>
        <div id="overlay_popup">&nbsp;</div>
        <div id="loading">&nbsp;<div id="loading-text">Vui lòng chờ...</div></div>
    </body>
</html>
<form name="frmKey">
    <input type="hidden" id="sskey"  value ="1763152193"/>
</form>
