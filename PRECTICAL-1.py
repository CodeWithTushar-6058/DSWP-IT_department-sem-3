<div class="console">
  <div class="top"> <span class="options">⦿ ○ ○</span> <span class="title">PSY - GANGNAM STYLE </span></div>
  <div class="tabs"> </div>
  <div class="text">
    <br>[06:24:55] Finished <span class="pink">'warm-up-hands'</span> after 8.81 s
    <br>[06:24:55] Finished <span class="pink">'warm-up-legs'</span> after 12 s
    <br>[06:24:55] Starting <span class="pink">'gangnam-style-dance'</span>...
    <br>[06:25:00] <span class="blue"> Calling PSY to start singing</span>
    <br> [06:25:02] <span class="orange">Eh, sexy lady 오-오-오-오 오빤 강남스타일</span>
    <br> [06:25:06] Strange cowboy moves
    <br>[06:24:55] Finished <span class="pink">'do-the-moves'</span> after 12 s
    <br> <span class="blue">? </span> Would you like to stop dancing soon as the song is ending? <span class="orange">Yes</span>
    <br> [06:25:14] Danced <span class="blue">234</span> steps, <span class="blue">234</span> passes, <span class="blue">0</span> failures: <span class="pink">SUCCESS </span>
    <br>
    <p class="typewriter"> root@PSY sudo <span class="pink"> dance-gangnam-style.exe</span></p>
    </span>
  </div>
</div>
<style>
  html {
  background: #222;
  font-family: helvetica;
  display: flex;
  align-items: center;
  justify-content: center;
  height: 100vh;

  .blue {
    color: #53d9d1;
  }
  .pink {
    color: #f27b9b;
  }
  .orange {
    color: #eb7132;
  }
  .console {
    border: 1px solid #444;
    border-radius: 3px;
    margin: 2rem;

    box-shadow: 0 0 15px 0px rgba(0, 0, 0, 0.75);
    .top {
      background: #333;
      color: #666;
      text-align: center;
      font-size: 12px;
      padding: 5px;
      .options {
        font-size: 16px;
        float: left;
      }
    }
    .text {
      font-family: courier;
      color: #fff;
      font-size: 14px;
      padding: 0.25rem;
    }
  }
}

.typewriter {
  overflow: hidden;
  width: fit-content;
  white-space: nowrap;
  border-right: 0.15em solid #eb7132;
  animation: typing 3s steps(15, end), blink-caret 0.75s step-end infinite;
}

/* The typing effect */
@keyframes typing {
  from {
    width: 0;
  }
  to {
    width: 60%;
  }
}

/* The typewriter cursor effect */
@keyframes blink-caret {
  from,
  to {
    border-color: transparent;
  }
  50% {
    border-color: orange;
  }
}

</style>