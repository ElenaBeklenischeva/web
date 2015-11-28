function hide(AIndex) {
	var tempChapter = document.getElementsByName("str"+AIndex);
	checked_headbox = document.getElementById('head_box' + AIndex);
	for (i = 0; i < tempChapter.length; i++) {
		if ( tempChapter[i].style.display == "") {
			tempChapter[i].style.display = "none";
		}

		if ( tempChapter[i].style.display == 'none' ) {
				tempChapter[i].style.display = 'table-row';
				document.getElementById("href" + AIndex).innerHTML = document.getElementById("href" + AIndex).innerHTML.replace('&#9654;','&#9660;');
		}
		else {
				tempChapter[i].style.display = 'none';
		}
	}
}

function checkCheckbox(AIndex) {
	chk = document.getElementsByName('blockbox' + AIndex);
	checked_headbox = document.getElementById('head_box' + AIndex).checked;

    if (checked_headbox) {
        for (i = 0; i < chk.length; i++){
            chk[i].checked = true ;
        }
    }
    else {
        for (i = 0; i < chk.length; i++){
        	chk[i].checked = false ;
        }
    }
    if (AIndex == 0) {
    	for (j = 1; j < 3; j++) {
    		checked_headbox = document.getElementById('head_box' + j).checked;
    		checked_headbox = true;
    		chk = document.getElementsByName('blockbox' + j);
    		for (i = 0; i < chk.length; i++){
            	chk[i].checked = true ;
        	}
    	}
    }
}

function changeFlag(ID){
	image = document.getElementById(ID)
	img1 = "file:///C:/Users/Lena/Documents/web/2/levelUp/images/flag1.png"
	img2 = "file:///C:/Users/Lena/Documents/web/2/levelUp/images/flag2.png"
	if (image.src == img1) {
		image.src = img2;
	} else {
		image.src = img1;
	}
}

function changeCheckBox(AIndex, IDbox){
	s_check_headbox = document.getElementById("head_box0");
	checked_headbox = document.getElementById("head_box"+AIndex);
	chk = document.getElementById(IDbox).checked;
	if (chk == false && chk != checked_headbox.checked) {
		checked_headbox.checked = false;
	}
	testList = document.getElementsByName("blockbox" + AIndex);
	count = 0;
	for (i = 0; i < testList.length; i++) {
		if (testList[i].checked == false) {
			count += 1;
		}
	}
	if (count < 2) {
		checked_headbox.checked = true;
	} else {
		checked_headbox.checked = false;
		s_check_headbox.checked = false;
	}
}