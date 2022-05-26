<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
<script type="text/JavaScript" src="/js/jquery-1.8.3.min.js"></script>

<script language="javascript">
function getDetailAddr(){
	// AJAX 상세주소 검색 요청
	$.ajax({
		url:"/sample/getDetailAddrApi.do"							// 고객사 API 호출할 Controller URL
		,type:"post"
		,data:$("#form").serialize() 								// 요청 변수 설정
		,dataType:"json"											// 데이터 결과 : JSON
		,success:function(jsonStr){									// jsonStr : 주소 검색 결과 JSON 데이터
			$("#list").html("");									// 결과 출력 영역 초기화
			var errCode = jsonStr.results.common.errorCode; 		// 응답코드
			var errDesc = jsonStr.results.common.errorMessage;		// 응답메시지
			if(errCode != "0"){ 									// 응답에러시 처리
				alert(errCode+"="+errDesc);
			}else{
				if(jsonStr!= null){
					makeListJson(jsonStr);							// 결과 JSON 데이터 파싱 및 출력
					makeSelectJson(jsonStr);
				}
			}
		}
		,error: function(xhr,status, error){
			alert("에러발생");										// AJAX 호출 에러
		}
	});
}

function makeListJson(jsonStr){
	var searchType = $("input[name='searchType']").val();
	var htmlStr = "";
	htmlStr += "<table>";
	// jquery를 이용한 JSON 결과 데이터 파싱
	$(jsonStr.results.juso).each(function(){
		htmlStr += "<tr>";
		htmlStr += "<td>"+this.admCd+"</td>";
		htmlStr += "<td>"+this.rnMgtSn+"</td>";
		htmlStr += "<td>"+this.udrtYn+"</td>";
		htmlStr += "<td>"+this.buldMnnm+"</td>";
		htmlStr += "<td>"+this.buldSlno+"</td>";
		htmlStr += "<td>"+this.dongNm+"</td>";
		if(searchType == "floorho"){
			htmlStr += "<td>"+this.floorNm+"</td>";
			htmlStr += "<td>"+this.hoNm+"</td>";
		}
		htmlStr += "</tr>";
	});
	htmlStr += "</table>";
	// 결과 HTML을 FORM의 결과 출력 DIV에 삽입
	$("#list").html(htmlStr);
}
function makeSelectJson(jsonStr){
	var dong_arry = $(jsonStr.results.juso).toArray();
	var dong_html = '<option value="">\"동\" 선택</option>';
	
	$(jsonStr.results.juso).each(function(){
		dong_html += '<option value="' +this.dongNm+ '">' +this.dongNm+ '</option>';
	});
	
	if(dong_arry.length == 0) dong_html = '<option value="none">\"동\" 표기 없음</option>';
	$("#detailAddrDong").html(dong_html);
}
</script>
</script>
<title>OPEN API 샘플 소스</title>
</head>
<body>
<form name="form" id="form" method="post">
    <input type="text" name="confmKey" value="TESTJUSOGOKR"/><!-- 요청 변수 설정 (승인키: 해당 테스트 승인키는 테스트 고정값만 제공) -->
	<input type="text" name="resultType" value="json"/> <!-- 요청 변수 설정 (검색결과형식 설정, json) --> 
	<input type="text" name="admCd" value="1135010200"/><!-- 요청 변수 설정 (행정구역코드) ※ 요청변수값은 도로명주소API, 좌표제공API, 주소DB 등에서 제공-->
	<input type="text" name="rnMgtSn" value="113503109006"/><!-- 요청 변수 설정 (도로명코드) --> 
	<input type="text" name="udrtYn" value="0"/><!-- 요청 변수 설정 (지하여부) -->
	<input type="text" name="buldMnnm" value="111"/><!-- 요청 변수 설정 (건물본번) --> 
	<input type="text" name="buldSlno" value="0"/><!-- 요청 변수 설정 (건물부번) -->
	<input type="text" name="searchType" value=""/><!-- 요청 변수 설정 (동층호 검색유형: dong, floorho) -->
	<input type="text" name="dongNm" value=""/><!-- 요청 변수 설정 (동: 층호 검색 시 입력) -->
	<input type="button" onClick="getDetailAddr();" value="상세주소 검색하기"/>
	<br/>
	<select id="detailAddrDong" title="상세주소(동)">
		<option value="">"동" 선택</option>
	</select>
	<div id="list" ></div><!-- 검색 결과 리스트 출력 영역 -->

</form>
</body>
</html>